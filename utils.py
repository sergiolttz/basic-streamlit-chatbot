from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

def get_role(message):
    """
    Function to get the role of a message.
    Args:
        messages(dict): Message dictionary containig 'role' and 'content' keys.
    Returns:
        str: Role of the message
    """
    if isinstance(message, HumanMessage):
        return "user"
    elif isinstance(message, AIMessage):
        return "assistant"
    elif isinstance(message, SystemMessage):
        return "system"
    else:
        return "user"
    
