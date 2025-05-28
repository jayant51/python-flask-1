from flask import Flask, jsonify, request
import os
import pymqi
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

queue_manager = 'qm-dev'  # Replace with your queue manager name
channel = 'ACEMQCLIENT'  # Replace with your channel name
host = 'qm-dev-ibm-mq'  # Replace with your MQ server host
port = ‘1414’  # Replace with your MQ server port
queue_name = 'BACKEND'  # Replace with your queue name
message = 'Hello, MQ!'

@app.route("/")
def hello():
    return "Jayant : Hello World!"

@app.route("/msg", method=["GET","POST"])
def msg():
    conn_info = '%s(%s)' % (host, port)

    try:
        qmgr = pymqi.connect(queue_manager, channel, conn_info)
        queue = pymqi.Queue(qmgr, queue_name)
        queue.put(message)
        print(f"Message sent to queue {queue_name}")
        queue.close()
        qmgr.disconnect()
    except pymqi.MQMIError as e:
        print(f"Error: {e}")
    return "Jayant : Hello Msg!"

@app.route("/res", methods=["GET"])
def res():
    if request.method == "GET":
        """
        data = {"ponum": 15, "lineitem": "keyboard"}
        """
        podata = {
            "OrderLines": {
                "OrderLine": {
                    "CarrierServiceCode": "UPS",
                    "ManufacturerName": "",
                    "DeliveryMethod": "SHP",
                    "RecevingNode": "",
                    "DeliveryCode": "Collect",
                    "ReqDeliveryDate": "2024-02-09",
                    "PrimeLineNo": "1",
                    "CustomerPONo": "C123456-4",
                    "Item": {
                        "CustomerItem": "",
                        "UnitOfMeasure": "EACH",
                        "ItemDesc": "Laptop 14",
                        "ManufacturerItem": "",
                        "ProductClass": "",
                        "ItemID": "Laptop 14",
                    },
                    "CarrierAccountNo": "123",
                    "CustomerLinePONo": "1",
                    "SubLineNo": "1",
                    "FillQuantity": "",
                    "SCAC": "UPS",
                    "ShipmentConsolidationGroupId": "",
                    "ItemGroupCode": "",
                    "ReqShipDate": "2024-02-20",
                    "LinePriceInfo": {"UnitPrice": "0", "IsPriceLocked": "Y"},
                    "ShipNode": "ATOS_Store",
                    "FreightTerms": "",
                    "OrderedQty": "1",
                    "LineType": "DS",
                    "FulfillmentType": "SHP",
                }
            }
        }
        return jsonify(podata)


if __name__ == "__main__":
    port = os.environ.get("FLASK_PORT") or 8080
    port = int(port)

    app.run(port=port, host="0.0.0.0")
