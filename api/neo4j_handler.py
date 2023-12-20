from sanic import json, Request
from sanic.views import HTTPMethodView

from utils.neo4j_handler import neo4j_helper


class Neo4jHandler(HTTPMethodView):

    @staticmethod
    async def post(request: Request):
        """
        {
            "cypher":"MATCH (p:Person {age: $age}) RETURN p.name AS name",
            "params":{"age":18}
        }
        :param request:
        :return:
        """
        request_json = request.json
        cypher = request_json.get('cypher')
        params = request_json.get('params', {})
        records = await neo4j_helper.execute(cypher=cypher, **params)
        return json({'records': records})
