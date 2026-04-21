import json

def load_knowledge():
    with open('knowledge_base.json','r')as f:
        return json.load(f)


def retrieve_answer(query):
    data = load_knowledge()
    query = query.lower()

    if any(word in query for word in ["price", "pricing", "plan", "plans", "cost"]):
        return data["pricing"]
    
    elif any(word in query for word in ["refund", "policy", "support"]):
        return data["policies"]
    else:
        return 'No relevant information found.'