import os


class DockerManager:
    def __init__(self, baseImagenName: str, baseImagenTag: str, KeyWord: str, localPort=80, interPort=8080):
        self.ContainerList = []
        self.localPort = localPort
        self.interPort = interPort
        self.baseImagenName = baseImagenName
        self.baseImagenTag = baseImagenTag
        self.KeyWord = KeyWord

    @staticmethod
    def dealLine(TextIn: str):
        y = ''
        flag = False
        for i in range(1, len(TextIn)-1, 1):
            if TextIn[i] == " " and TextIn[i-1] != " " and TextIn[i+1] != " ":
                TextIn = TextIn[:i] + "_" + TextIn[i+1:]
        for i in TextIn:
            if i == ' ' and flag:
                continue
            if i != ' ' and flag:
                flag = False
            y += i
            if i == ' ':
                flag = True

        x = y.split(" ")
        for i in range(len(x)-1, -1, -1):
            if len(x[i]) == 0:
                x.pop(i)
        return x

    def ShowContainerList(self):
        DockerList = {}
        res = os.popen("docker ps -a").read().split("\n")
        for i in range(1, len(res) - 1, 1):
            data = self.dealLine(res[i])
            DockerList[data[-1]] = {
                "Name": data[-1],
                "Status": data[3]
            }
        return DockerList

    def StartContainer(self, ContainerID: str, interPort: int):
        ContainerDict = self.ShowContainerList()
        if self.KeyWord + str(ContainerID) in ContainerDict:
            self.StopContainer(self.KeyWord + str(ContainerID))
            self.RemoveContainer(self.KeyWord + str(ContainerID))
        return os.popen("docker run --name {} -d -p {}:{} {}:{}".format(self.KeyWord + str(ContainerID), interPort, self.localPort, self.baseImagenName, self.baseImagenTag)).read()

    def StopContainer(self, ContainerName: str):
        ContainerDict = self.ShowContainerList()
        for Name in ContainerDict:
            if ContainerName == Name:
                return os.popen("docker stop {}".format(ContainerName)).read()

    def RemoveContainer(self, ContainerName: str):
        ContainerDict = self.ShowContainerList()
        for Name in ContainerDict:
            if ContainerName == Name:
                return os.popen("docker rm {}".format(ContainerName)).read()

    def CheckTimeOutContainer(self):
        flag = "None"
        ContainerDict = self.ShowContainerList()
        for Name in ContainerDict:
            if self.KeyWord not in Name:
                continue
            Time = str(ContainerDict[Name]["Status"])
            if Time.split("_")[-2] not in ["minutes", "seconds", "second", "minute"]:
                self.StopContainer(Name)
                self.RemoveContainer(Name)
                flag = "Yes"
        return flag

    def RemoveAllRelatedContainers(self):
        ContainerDict = self.ShowContainerList()
        for Name in ContainerDict:
            if self.KeyWord not in Name:
                continue
            self.StopContainer(Name)
            self.RemoveContainer(Name)


if __name__ == '__main__':
    X = DockerManager("edm", "v0", "haha")
    z = X.StartContainer("0", 10)
    X.ShowContainerList()
    print(z)