from flask import Flask, redirect
from utils.dockerManager import DockerManager
import time
app = Flask(__name__)
X = DockerManager("edm", "v0", "haha")
X.RemoveAllRelatedContainers()
PortNow = 27231


@app.route("/")
def allocate():
    global PortNow
    PortNow += 1
    if PortNow > 30000:
        PortNow = 27230
    start = X.StartContainer(PortNow, PortNow)
    print(start)
    routeCheck = X.CheckTimeOutContainer()
    print(routeCheck)
    time.sleep(0.8)
    print(X.ShowContainerList())
    return redirect("http://127.0.0.1:{}".format(PortNow))


if __name__ == '__main__':
    app.run(debug=True, port=4352)
