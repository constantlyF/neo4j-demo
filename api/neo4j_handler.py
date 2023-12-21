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

    @staticmethod
    async def get(request):
        query = """
        MATCH (n)-[r]->(m)
        RETURN n, r, m
        LIMIT 100
        """
        result = await neo4j_helper.execute(cypher=query)
        data = {'nodes': [], 'links': []}
        for record in result:
            data['nodes'].append(
                {'id': record['n'].id, 'label': list(record['n'].labels)[0], 'properties': dict(record['n'])})
            data['nodes'].append(
                {'id': record['m'].id, 'label': list(record['m'].labels)[0], 'properties': dict(record['m'])})
            data['links'].append({'source': record['n'].id, 'target': record['m'].id, 'label': record['r'].type})
        return json(data)
