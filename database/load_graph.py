from database.neo4j_connection import driver


def load_graph():

    query = """

    MERGE (b:Batch {id:'B004'})

    MERGE (r:Reactor {name:'Reactor A'})

    MERGE (c:CoolingSystem {name:'Cooling Pump 1'})

    MERGE (f:Failure {name:'Cooling Failure'})


    MERGE (b)-[:USES]->(r)

    MERGE (r)-[:CONNECTED_TO]->(c)

    MERGE (c)-[:CAUSED]->(f)

    """


    with driver.session() as session:

        session.run(query)


    print(

        "Knowledge graph loaded."

    )


if __name__ == "__main__":

    load_graph()