// 文件路径: ui/map/qwebchannel.js
"use strict";

var QWebChannelMessageTypes = {
    signal: 1,
    propertyUpdate: 2,
    init: 3,
    idle: 4,
    debug: 5,
    invokeMethod: 6,
    connectToSignal: 7,
    disconnectFromSignal: 8,
    setProperty: 9,
    response: 10,
};

var QWebChannel = function(transport, initCallback) {
    if (typeof transport !== "object" || typeof transport.send !== "function") {
        console.error("The QWebChannel expects a transport object with a send function and onmessage callback property.");
        return;
    }
    this.transport = transport;
    this.send = function(data) {
        if (typeof(data) !== "string") {
            data = JSON.stringify(data);
        }
        this.transport.send(data);
    }
    this.transport.onmessage = function(message) {
        var data = message.data;
        if (typeof data === "string") {
            data = JSON.parse(data);
        }
        switch (data.type) {
            case QWebChannelMessageTypes.signal:
                this.handleSignal(data);
                break;
            case QWebChannelMessageTypes.response:
                this.handleResponse(data);
                break;
            case QWebChannelMessageTypes.propertyUpdate:
                this.handlePropertyUpdate(data);
                break;
            default:
                console.error("invalid message received:", message.data);
                break;
        }
    }.bind(this);

    this.execCallbacks = {};
    this.execId = 0;
    this.exec = function(data, callback) {
        if (!callback) {
            this.send(data);
            return;
        }
        if (this.execId === Number.MAX_VALUE) {
            this.execId = Number.MIN_VALUE;
        }
        if (data.hasOwnProperty("id")) {
            console.error("Cannot exec message with property id: " + JSON.stringify(data));
            return;
        }
        data.id = this.execId++;
        this.execCallbacks[data.id] = callback;
        this.send(data);
    };

    this.objects = {};
    this.handleSignal = function(message) {
        var object = this.objects[message.object];
        if (object) {
            object.signalEmitted(message.signal, message.args);
        } else {
            console.warn("Unhandled signal: " + message.object + "::" + message.signal);
        }
    }
    this.handleResponse = function(message) {
        if (!message.hasOwnProperty("id")) {
            console.error("Invalid response message received: ", JSON.stringify(message));
            return;
        }
        this.execCallbacks[message.id](message.data);
        delete this.execCallbacks[message.id];
    }
    this.handlePropertyUpdate = function(message) {
        for (var i in message.data) {
            var data = message.data[i];
            var object = this.objects[data.object];
            if (object) {
                object.propertyUpdate(data.signals, data.properties);
            } else {
                console.warn("Unhandled property update: " + data.object + "::" + data.signal);
            }
        }
        this.exec({type: QWebChannelMessageTypes.idle});
    }

    this.debug = function(message) {
        this.send({type: QWebChannelMessageTypes.debug, data: message});
    };

    this.exec({type: QWebChannelMessageTypes.init}, function(data) {
        for (var objectName in data) {
            var object = new QObject(objectName, data[objectName], this);
        }
        if (initCallback) {
            initCallback(this);
        }
        this.exec({type: QWebChannelMessageTypes.idle});
    }.bind(this));
};

function QObject(name, data, webChannel) {
    this.__id__ = name;
    webChannel.objects[name] = this;
    this.__objectSignals__ = {};
    this.__propertyCache__ = {};

    var object = this;

    this.unwrapQObject = function(response) {
        if (response instanceof Array) {
            var ret = new Array(response.length);
            for (var i = 0; i < response.length; ++i) {
                ret[i] = object.unwrapQObject(response[i]);
            }
            return ret;
        }
        if (!response
            || !response["__QObject*__"]
            || response.id === undefined) {
            return response;
        }
        var objectId = response.id;
        if (webChannel.objects[objectId])
            return webChannel.objects[objectId];
        if (!response.data) {
            console.error("Cannot unwrap unknown QObject " + objectId + " without data.");
            return;
        }
        return new QObject( objectId, response.data, webChannel );
    }

    this.unwrapProperties = function() {
        for (var propertyIdx in object.__propertyCache__) {
            object.__propertyCache__[propertyIdx] = object.unwrapQObject(object.__propertyCache__[propertyIdx]);
        }
    }

    function addSignal(signalData, isPropertyNotifySignal) {
        var signalName = signalData[0];
        var signalIndex = signalData[1];
        object[signalName] = {
            connect: function(callback) {
                if (typeof(callback) !== "function") {
                    console.error("Bad callback given to connect to signal " + signalName);
                    return;
                }
                object.__objectSignals__[signalIndex] = object.__objectSignals__[signalIndex] || [];
                object.__objectSignals__[signalIndex].push(callback);
                if (!isPropertyNotifySignal && signalName !== "destroyed") {
                    webChannel.exec({
                        type: QWebChannelMessageTypes.connectToSignal,
                        object: object.__id__,
                        signal: signalIndex
                    });
                }
            },
            disconnect: function(callback) {
                if (typeof(callback) !== "function") {
                    console.error("Bad callback given to disconnect from signal " + signalName);
                    return;
                }
                object.__objectSignals__[signalIndex] = object.__objectSignals__[signalIndex] || [];
                var idx = object.__objectSignals__[signalIndex].indexOf(callback);
                if (idx === -1) {
                    console.error("Cannot find connection of signal " + signalName + " to " + callback.name);
                    return;
                }
                object.__objectSignals__[signalIndex].splice(idx, 1);
                if (!isPropertyNotifySignal && object.__objectSignals__[signalIndex].length === 0) {
                    webChannel.exec({
                        type: QWebChannelMessageTypes.disconnectFromSignal,
                        object: object.__id__,
                        signal: signalIndex
                    });
                }
            }
        };
    }

    function invokeMethod(methodName, args) {
        webChannel.exec({
            type: QWebChannelMessageTypes.invokeMethod,
            object: object.__id__,
            method: methodName,
            args: args
        }, function(response) {
            if (response !== undefined) {
                var result = object.unwrapQObject(response);
                if (args.length > 0 && typeof(args[args.length - 1]) === "function") {
                    args[args.length - 1](result);
                }
            }
        });
    }

    function bindGetterSetter(propertyInfo) {
        var propertyIndex = propertyInfo[0];
        var propertyName = propertyInfo[1];
        var notifySignalData = propertyInfo[2];
        object.__propertyCache__[propertyIndex] = propertyInfo[3];
        if (notifySignalData) {
            if (notifySignalData[0] === 1) {
                notifySignalData[0] = propertyName + "Changed";
            }
            addSignal(notifySignalData, true);
        }
        Object.defineProperty(object, propertyName, {
            configurable: true,
            get: function () {
                var propertyValue = object.__propertyCache__[propertyIndex];
                if (propertyValue === undefined) {
                    console.warn("Undefined value in property cache for property \"" + propertyName + "\" in object " + object.__id__);
                }
                return propertyValue;
            },
            set: function(value) {
                if (value === undefined) {
                    console.warn("Property setter for " + propertyName + " called with undefined value!");
                    return;
                }
                object.__propertyCache__[propertyIndex] = value;
                webChannel.exec({
                    type: QWebChannelMessageTypes.setProperty,
                    object: object.__id__,
                    property: propertyIndex,
                    value: value
                });
            }
        });
    }

    for (var i = 0; i < data[0].length; ++i) {
        addSignal(data[0][i], false);
    }
    for (var i = 0; i < data[1].length; ++i) {
        invokeMethod(data[1][i][0], []);
        object[data[1][i][0]] = function(methodName) {
            return function() {
                invokeMethod(methodName, Array.prototype.slice.call(arguments));
            };
        }(data[1][i][0]);
    }
    for (var i = 0; i < data[2].length; ++i) {
        bindGetterSetter(data[2][i]);
    }
    object.unwrapProperties();
    
    this.signalEmitted = function(signalName, signalArgs) {
        var callbacks = object.__objectSignals__[signalName];
        if (callbacks) {
            for (var i = 0; i < callbacks.length; ++i) {
                callbacks[i].apply(object, object.unwrapQObject(signalArgs));
            }
        }
    }
    this.propertyUpdate = function(signals, propertyMap) {
        for (var propertyIndex in propertyMap) {
            var propertyValue = propertyMap[propertyIndex];
            object.__propertyCache__[propertyIndex] = propertyValue;
        }
        object.unwrapProperties();
        for (var signalName in signals) {
            var signalArgs = signals[signalName];
            object.signalEmitted(signalName, signalArgs);
        }
    }
}