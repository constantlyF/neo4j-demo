import multiprocessing

from sanic import Sanic, json, Request

from api.neo4j_handler import Neo4jHandler

# 创建一个Sanic应用
app = Sanic('neo4j-demo')


@app.get("/")
async def index(request: Request):
    return json({"code": "ok"}, status=200)


app.add_route(
    Neo4jHandler.as_view(), uri='/execute'
)

# 启动应用
if __name__ == '__main__':
    cpus = 2 if multiprocessing.cpu_count() > 2 else multiprocessing.cpu_count()
    app.run(host='0.0.0.0', port=8080, workers=cpus, access_log=False)
