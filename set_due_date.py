"""
This module provides functions to modify existing reminders in the Apple Reminders app.
It includes functionality to randomly select a reminder and set its due date.
"""
import subprocess

def run_shortcut(shortcut_name):
    """
    Executes the specified Apple Shortcut by name.

    Args:
        shortcut_name (str): The name of the Apple Shortcut to run.

    Returns:
        str: The output from the Shortcut execution.
    """
    try:
        result = subprocess.run(
            ["shortcuts", "run", shortcut_name],
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running shortcut: {e}")
        return None

if __name__ == "__main__":
# ショートカットの作成方法
# ショートカットアプリを開く。
# 新しいショートカットを作成:
# 「リマインダーの取得」アクションを追加して、指定リストの全てのリマインダーを取得。
# 「リストからランダムな項目を取得」アクションでランダムに選択。
# 「リマインダーを編集」アクションで期限を「今日」に設定。
# 名前を設定:
# 例えば「RandomSelectReminder」と命名。

    SHORTCUT_NAME = "RandomSelectReminder"  # ショートカット名
    output = run_shortcut(SHORTCUT_NAME)
    if output:
        print("Shortcut output:", output)
