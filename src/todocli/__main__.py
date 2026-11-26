"""Command-line interface."""
import json
from pathlib import Path
import click

# Tentukan lokasi file penyimpanan tugas di folder home user
TODO_FILE = Path.home() / ".todocli_tasks.json"

def load_tasks() -> list:
    """Membaca daftar tugas dari file JSON."""
    if TODO_FILE.exists():
        try:
            with open(TODO_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                # Konversi format lama (string) ke format baru (dict dengan status 'done')
                if data and isinstance(data[0], str):
                    return [{"text": task, "done": False} for task in data]
                return data
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks: list) -> None:
    """Menyimpan daftar tugas ke file JSON."""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


@click.group()
@click.version_option()
def main() -> None:
    """Todo Cli."""
    pass


@main.command()
@click.argument("task")
def add(task: str) -> None:
    """Add a new task to your todo list."""
    tasks = load_tasks()
    tasks.append({"text": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Berhasil menambahkan tugas: '{task}'")


@main.command(name="list")
def list_tasks() -> None:
    """List all your todo tasks."""
    tasks = load_tasks()
    if not tasks:
        click.echo("Belum ada tugas yang tersimpan.")
        return
    
    click.echo("Daftar Tugas Kamu:")
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        click.echo(f"{index}. [{status}] {task['text']}")


@main.command()
@click.argument("index", type=int)
def done(index: int) -> None:
    """Mark a task as completed."""
    tasks = load_tasks()
    if not tasks:
        click.echo("Belum ada tugas.")
        return
    
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Tugas nomor {index} ditandai selesai! 🎉")
    else:
        click.echo(f"Nomor tugas {index} tidak valid.")


@main.command()
@click.argument("index", type=int)
def delete(index: int) -> None:
    """Delete a task by its number."""
    tasks = load_tasks()
    if not tasks:
        click.echo("Belum ada tugas untuk dihapus.")
        return
    
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        click.echo(f"Berhasil menghapus tugas: '{removed_task['text']}'")
    else:
        click.echo(f"Nomor tugas {index} tidak valid.")


if __name__ == "__main__":
    main(prog_name="todocli")