from graphs.workflow import graph


query = input("Ask something: ")


result = graph.invoke(
    {
        "query": query
    }
)

print()

print(result)