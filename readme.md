# 非常的不清真

假设，某A把Easy Data Maker用docker部署在服务器上，然后跑起来了

然后再假设，某B和某C同时访问服务器，同时生成数据，那会发生什么捏？同时写入.in .out文件？其实我也不知道，反正一定会出问题。

那么再假设，如果某B访问服务器的时候，让服务器给某B开一个docker，某C访问服务器的时候，让服务器给某C开一个docker，还会不会有问题捏？

好像没问题吧，那就写一个算了

# 部署

先把[Easy Data Maker](https://github.com/Andrew82106/EasyDataMaker-For_UOJ-)部署好，镜像名字和标签需要设置为``edm:v0``

然后把这坨代码拷过去，目录下跑：

```bash
pip install -r requirements.txt
gunicorn main:app -c ./gunicorn.conf.py
```

或者也可以搞成docker试试：

```bash
sudo docker build -f ./DockerFile -t allocator:v0 .
docker run -d -p 8080:4352 allocator:v0
```