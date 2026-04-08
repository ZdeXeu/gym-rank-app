import flet as ft
import json
import os

data = {}
xp = {}

XP_PER_LEVEL = 1000
SAVE_FILE = "data.json"

MUSCLE_COLORS = {
    "Biceps": ft.Colors.BLUE,
    "Triceps": ft.Colors.GREEN,
    "Hrudník": ft.Colors.RED,
    "Záda": ft.Colors.ORANGE,
    "Ramena": ft.Colors.PURPLE,
    "Nohy": ft.Colors.BROWN,
    "Core": ft.Colors.CYAN,
}

EXERCISES = {
    "Biceps": [
        {"name": "Bicepsový zdvih", "multiplier": 1.5},
        {"name": "Hammer curl", "multiplier": 1.5},
        {"name": "EZ curl", "multiplier": 1.4},
        {"name": "Concentration curl", "multiplier": 1.7},
        {"name": "Cable curl", "multiplier": 1.6},
        {"name": "Preacher curl", "multiplier": 1.6},
        {"name": "Incline dumbbell curl", "multiplier": 1.7},
        {"name": "Reverse curl", "multiplier": 1.8},
        {"name": "Spider curl", "multiplier": 1.7},
        {"name": "Machine curl", "multiplier": 1.5},
    ],

    "Triceps": [
        {"name": "Kliky na bradlech", "multiplier": 1.3},
        {"name": "Pushdown", "multiplier": 1.4},
        {"name": "Francouzský tlak", "multiplier": 1.5},
        {"name": "Overhead extension", "multiplier": 1.5},
        {"name": "Close grip bench", "multiplier": 1.2},
        {"name": "Kickback", "multiplier": 1.8},
        {"name": "Rope pushdown", "multiplier": 1.4},
        {"name": "Skullcrusher", "multiplier": 1.5},
        {"name": "Machine triceps", "multiplier": 1.5},
        {"name": "Bench dips", "multiplier": 1.6},
    ],

    "Hrudník": [
        {"name": "Bench press", "multiplier": 1.0},
        {"name": "Incline bench", "multiplier": 1.1},
        {"name": "Decline bench", "multiplier": 1.1},
        {"name": "Kliky", "multiplier": 1.3},
        {"name": "Rozpažky", "multiplier": 1.8},
        {"name": "Cable fly", "multiplier": 1.7},
        {"name": "Chest press machine", "multiplier": 1.2},
        {"name": "Incline dumbbell press", "multiplier": 1.2},
        {"name": "Decline dumbbell press", "multiplier": 1.2},
        {"name": "Pec deck", "multiplier": 1.6},
    ],

    "Záda": [
        {"name": "Shyby", "multiplier": 1.3},
        {"name": "Lat pulldown", "multiplier": 1.2},
        {"name": "Přítahy v předklonu", "multiplier": 1.1},
        {"name": "Deadlift", "multiplier": 0.9},
        {"name": "Seated row", "multiplier": 1.2},
        {"name": "T-bar row", "multiplier": 1.1},
        {"name": "Straight arm pulldown", "multiplier": 1.4},
        {"name": "Machine row", "multiplier": 1.2},
        {"name": "Pull-over", "multiplier": 1.5},
        {"name": "Face pull", "multiplier": 1.6},
    ],

    "Ramena": [
        {"name": "Tlaky nad hlavu", "multiplier": 1.1},
        {"name": "Upažování", "multiplier": 2.0},
        {"name": "Předpažování", "multiplier": 1.8},
        {"name": "Arnold press", "multiplier": 1.2},
        {"name": "Rear delt fly", "multiplier": 1.9},
        {"name": "Cable lateral raise", "multiplier": 2.0},
        {"name": "Machine shoulder press", "multiplier": 1.2},
        {"name": "Front raise plate", "multiplier": 1.8},
        {"name": "Upright row", "multiplier": 1.4},
        {"name": "Reverse pec deck", "multiplier": 1.9},
    ],

    "Nohy": [
        {"name": "Dřepy", "multiplier": 1.2},
        {"name": "Leg press", "multiplier": 1.1},
        {"name": "Výpady", "multiplier": 1.5},
        {"name": "Zakopávání", "multiplier": 1.7},
        {"name": "Předkopávání", "multiplier": 1.7},
        {"name": "Rumunský mrtvý tah", "multiplier": 1.1},
        {"name": "Hip thrust", "multiplier": 1.2},
        {"name": "Výpony lýtek", "multiplier": 1.8},
        {"name": "Bulharské dřepy", "multiplier": 1.6},
        {"name": "Hack squat", "multiplier": 1.2},
    ],

    "Core": [
        {"name": "Plank", "multiplier": 2.0},
        {"name": "Sedy-lehy", "multiplier": 1.5},
        {"name": "Zkracovačky", "multiplier": 1.6},
        {"name": "Leg raises", "multiplier": 1.7},
        {"name": "Russian twist", "multiplier": 1.8},
        {"name": "Hanging leg raises", "multiplier": 1.9},
        {"name": "Cable crunch", "multiplier": 1.6},
        {"name": "Ab wheel", "multiplier": 2.0},
        {"name": "Mountain climbers", "multiplier": 1.7},
        {"name": "V-ups", "multiplier": 1.8},
    ]
}


def save_data():
    with open(SAVE_FILE, "w") as f:
        json.dump({"data": data, "xp": xp}, f)


def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            content = json.load(f)
            data.update(content.get("data", {}))
            xp.update(content.get("xp", {}))


def main(page: ft.Page):
    page.title = "Gym Rank"
    page.theme_mode = "dark"
    page.padding = 0
    page.vertical_alignment = "start"

    load_data()

    selected_muscle = None
    selected_exercise = None

    weight_input = ft.TextField(label="Váha (kg)", border_radius=10)
    reps_input = ft.TextField(label="Opakování", border_radius=10)

    result_text = ft.Text("")
    last_text = ft.Text("")
    pr_text = ft.Text("")

    # 🔥 SCROLL CONTAINER (hlavní fix)
    main_column = ft.Column(spacing=15)
    main_column.spacing = 10
    scroll_view = ft.Column(
        controls=[main_column],
        scroll=ft.ScrollMode.ALWAYS,
        expand=True
    )

    def get_level(m):
        total = xp.get(m, 0)
        return total // XP_PER_LEVEL + 1, (total % XP_PER_LEVEL) / XP_PER_LEVEL

    def get_stats(m, ex):
        records = [r for r in data.get(m, []) if r["exercise"] == ex]
        if not records:
            return None, None
        return records[-1], max(records, key=lambda r: r["weight"] * r["reps"])

    # 🟢 SVALY
    def show_muscles():
        main_column.controls.clear()

        main_column.controls.append(
            ft.Text("💪 Gym Rank", size=30, weight="bold")
        )

        for m in EXERCISES:
            lvl, prog = get_level(m)

            main_column.controls.append(
                ft.Card(
                    elevation=6,
                    content=ft.Container(
                        padding=15,
                        border_radius=20,
                        bgcolor=MUSCLE_COLORS.get(m),
                        content=ft.Column([
                            ft.Text(m, size=20, weight="bold"),
                            ft.Text(f"Level {lvl}"),
                            ft.ProgressBar(value=prog, height=10),
                        ]),
                        on_click=lambda e, m=m: show_exercises(m),
                    )
                )
            )

        page.update()

    # 🟡 CVIKY
    def show_exercises(m):
        nonlocal selected_muscle
        selected_muscle = m

        main_column.controls.clear()

        main_column.controls.append(
            ft.Column([
                ft.Text(m, size=28, weight="bold"),
                ft.Text("Vyber cvik", size=14, color=ft.Colors.GREY)
            ], spacing=0)
        )

        for ex in EXERCISES[m]:
            main_column.controls.append(
                ft.Container(
                    padding=12,
                    border_radius=20,
                    bgcolor=ft.Colors.BLUE_GREY_900,
                    on_click=lambda e, ex=ex: show_form(ex),
                    content=ft.Row([
                        # levá část (název)
                        ft.Column([
                            ft.Text(ex["name"], size=18, weight="bold"),
                            ft.Text("Klikni pro zápis", size=12, color=ft.Colors.GREY)
                        ], expand=True, spacing=2),

                        # pravá část (XP badge)
                        ft.Container(
                            padding=8,
                            border_radius=12,
                            bgcolor=MUSCLE_COLORS.get(m),
                            content=ft.Text(f"x{ex['multiplier']}", size=12)
                        )
                    ])
                )
            )

        main_column.controls.append(
            ft.ElevatedButton("⬅ Zpět", height=50, on_click=lambda e: show_muscles())
        )

        page.update()

    # 🔵 FORM
    def show_form(ex):
        nonlocal selected_exercise
        selected_exercise = ex

        name = ex["name"]

        main_column.controls.clear()

        last, pr = get_stats(selected_muscle, name)

        last_text.value = f"Poslední: {last['weight']}kg × {last['reps']}" if last else "Poslední: žádný"
        pr_text.value = f"PR: {pr['weight']}kg × {pr['reps']}" if pr else "PR: žádný"

        main_column.controls.extend([
            ft.Text(name, size=24, weight="bold"),
            ft.Text(f"XP x{ex['multiplier']}"),

            weight_input,
            reps_input,

            ft.ElevatedButton(
                "Uložit trénink",
                height=55,
                on_click=add_record
            ),

            ft.Divider(),

            last_text,
            pr_text,
            result_text,

            ft.ElevatedButton("⬅ Zpět", on_click=lambda e: show_exercises(selected_muscle))
        ])

        page.update()

    # ➕ ULOŽENÍ
    def add_record(e):
        m = selected_muscle
        ex = selected_exercise
        name = ex["name"]

        try:
            w = int(weight_input.value)
            r = int(reps_input.value)
        except:
            result_text.value = "Zadej čísla!"
            page.update()
            return

        data.setdefault(m, []).append({"exercise": name, "weight": w, "reps": r})

        gained = int(w * r * ex["multiplier"])
        xp[m] = xp.get(m, 0) + gained

        result_text.value = f"+{gained} XP"

        last, pr = get_stats(m, name)
        last_text.value = f"Poslední: {last['weight']}kg × {last['reps']}"
        pr_text.value = f"PR: {pr['weight']}kg × {pr['reps']}"

        weight_input.value = ""
        reps_input.value = ""

        save_data()
        page.update()

    # 📱 ROOT (důležité!)
    page.add(
        ft.Container(
            expand=True,
            content=scroll_view
        )
    )

    show_muscles()


ft.app(target=main)