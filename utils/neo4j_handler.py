import asyncio
import threading

from neo4j import AsyncGraphDatabase

from config.config_manage import NEO4J_CONFIG

URI = f"bolt://{NEO4J_CONFIG['host']}:{NEO4J_CONFIG['port']}"
AUTH = (NEO4J_CONFIG['username'], str(NEO4J_CONFIG['password']))
DATABASE = (NEO4J_CONFIG['database'])


class Neo4jHelper:
    _lock = threading.Lock()

    def __init__(self):
        if not hasattr(self, 'driver'):
            with self._lock:
                if not hasattr(self, 'driver'):
                    self._driver = AsyncGraphDatabase.driver(uri=URI, auth=AUTH, database=DATABASE)

    async def close(self):
        await self._driver.close()

    async def execute(self, cypher, **kwargs):
        """Execute a Cypher statement

        Args:
            cypher (str): Cypher statement

        Returns:
            _records

        Examples:
            records = await neo4j_helper.execute('MATCH (p:Person {age: $age}) RETURN p.name AS name', age=18)
            for person in records:
                print(person.data())
        """
        _records, _summary, _keys = await self._driver.execute_query(cypher, **kwargs)
        return _records


neo4j_helper = Neo4jHelper()


async def main():
    cql_del = "match (p:%) detach delete p"
    cql_create = """
                CREATE 
                (tom:Person {name: 'tom', age: 18}),
                (jack:Person {name: 'jack', age: 19}),
                (rose:Person {name: 'rose', age: 19})

                CREATE
                (m1:Movie {name: '泰坦尼克号'}),
                (m2:Movie {name: '猫抓老鼠'})

                CREATE
                (tom)-[:ACTED_IN {roles:['TOM']}]->(m1),
                (jack)-[:ACTED_IN {roles:['JACK']}]->(m2),
                (rose)-[:ACTED_IN {roles:['ROSE']}]->(m2)
                """

    records = await neo4j_helper.execute('MATCH (p:Person {age: $age}) RETURN p.name AS name', age=18)
    for person in records:
        print(person.data())


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
