
import json
import logging

import azure.functions as func


def main(event: func.EventGridEvent):
    logging.info("Function triggered to process a message: ", event.get_body())
    logging.info(f"  EnqueuedTimeUtc = {event.enqueued_time}")
    logging.info(f"  SequenceNumber = {event.sequence_number}")
    logging.info(f"  Offset = {event.offset}")

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info("Python EventGrid trigger processed an event: {}".format(result))

    # Metadata
    for key in event.metadata:
        logging.info(f"Metadata: {key} = {event.metadata[key]}")



