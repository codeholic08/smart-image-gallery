import boto3
from config import Config

lexbot_client = boto3.client('lexv2-runtime', region_name=Config.AWS_REGION)

def understand_query(query):
    try:
        lex_response = lexbot_client.recognize_text(
            botId=Config.LEX_BOT_ID,
            botAliasId=Config.LEX_BOT_ALIAS_ID,
            localeId='en_US',
            sessionId="test",
            text=query
        )
        return [slot['value']['originalValue'] for slot in lex_response['sessionState']['intent']['slots'].values() if slot]
    except Exception as e:
        raise Exception(f"Failed to understand query with Lex: {str(e)}")