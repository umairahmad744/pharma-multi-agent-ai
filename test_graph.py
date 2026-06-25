from graphs.workflow import graph

result = graph.invoke(
    {
        "query": "What is pharmaceutical quality control?"
    }
)

print(result)