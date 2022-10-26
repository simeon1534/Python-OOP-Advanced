from datetime import timedelta
from report_formatter import format_report
from report_generator import generate_report


def main():

    report = generate_report(duration=timedelta(seconds=10))
    formatted = format_report(report)
    print(formatted)
    #send_email(formatted)


if __name__ == '__main__':
    main()
