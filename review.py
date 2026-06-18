import subprocess
from datetime import date
import os

def main():
    result = subprocess.run(
        ['git', '-c', 'core.quotepath=false', 'log',
         '--pretty=format:DATE:%ad|%s', '--date=short', '--name-only'],
        capture_output=True, text=True, encoding='utf-8'
    )

    today = date.today()

    add_days    = {14: '2주일 후', 30: '1달 후', 90: '3달 후'}
    review_days = {1: '1일 후',   7: '1주일 후', 21: '3주일 후'}

    all_days = set(add_days) | set(review_days)
    schedule = {'add': {d: [] for d in add_days},
                'review': {d: [] for d in review_days}}

    current_date = None
    current_message = None

    for line in result.stdout.strip().split('\n'):
        line = line.strip()
        if line.startswith('DATE:'):
            parts = line[5:].split('|', 1)
            try:
                current_date = date.fromisoformat(parts[0])
                current_message = parts[1] if len(parts) > 1 else ''
            except ValueError:
                current_date = None
        elif line and current_date:
            days_ago = (today - current_date).days
            filename = os.path.basename(line)
            if current_message.startswith('[Add]') and days_ago in add_days:
                schedule['add'][days_ago].append(filename)
            elif current_message.startswith(('[Refactor]', '[Review]')) and days_ago in review_days:
                schedule['review'][days_ago].append(filename)

    print(f"=== 오늘의 복습 목록 ({today}) ===\n")

    has_review = False

    for days, label in add_days.items():
        if schedule['add'][days]:
            has_review = True
            print(f"[Add {label}]")
            for f in schedule['add'][days]:
                print(f"  - {f}")
            print()

    for days, label in review_days.items():
        if schedule['review'][days]:
            has_review = True
            print(f"[Refactor/Review {label}]")
            for f in schedule['review'][days]:
                print(f"  - {f}")
            print()

    if not has_review:
        print("오늘 복습할 문제가 없습니다.")

if __name__ == '__main__':
    main()
