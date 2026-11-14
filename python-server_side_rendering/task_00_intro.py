#!/usr/bin/python3
"""
Task 0: Creating a Simple Templating Program
"""


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a
    template and a list of attendees.
    """
    if not isinstance(template, str):
        print(f"Error: Template must be a string, "
              f"got {type(template).__name__}.")
        return
    if not isinstance(attendees, list) or \
       not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name")
        name = name if name is not None else "N/A"

        event_title = attendee.get("event_title")
        event_title = event_title if event_title is not None else "N/A"

        event_date = attendee.get("event_date")
        event_date = event_date if event_date is not None else "N/A"

        event_loc = attendee.get("event_location")
        event_location = event_loc if event_loc is not None else "N/A"

        try:
            content = template.format(
                name=name,
                event_title=event_title,
                event_date=event_date,
                event_location=event_location
            )
        except KeyError:
            content = template
            content = content.replace("{name}", str(name))
            content = content.replace("{event_title}", str(event_title))
            content = content.replace("{event_date}", str(event_date))
            content = content.replace(
                "{event_location}", str(event_location)
            )

        output_filename = f"output_{index}.txt"

        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")
