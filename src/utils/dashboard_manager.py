from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

class DashboardManager:
    """
    Rich kütüphanesi ile terminal tabanlı görev kontrol paneli.
    """
    def __init__(self):
        self.console = Console()
        self.layout = Layout()
        self._init_layout()

    def _init_layout(self):
        self.layout.split(
            Layout(name="header", size=3),
            Layout(name="main", size=20),
            Layout(name="footer", size=3)
        )
        self.layout["main"].split_row(
            Layout(name="status", ratio=1),
            Layout(name="logs", ratio=2)
        )

    def generate_header(self):
        return Panel(
            Text("ASTROBIO-EDGE : MISSION CONTROL (v0.5.0 SOVEREIGNTY)", justify="center", style="bold blue"),
            style="white"
        )

    def generate_status_table(self, nodes_data, swarm_status):
        table = Table(title="Sürü Durumu")
        table.add_column("Düğüm", style="cyan")
        table.add_column("Batarya", style="green")
        table.add_column("Sıcaklık", style="yellow")
        table.add_column("Sağlık", style="magenta")
        table.add_column("Bulgu", style="bold red")

        for node in nodes_data:
            finding = "POZİTİF" if node.get("is_positive") else "NOMİNAL"
            finding_style = "bold red" if node.get("is_positive") else "green"
            
            table.add_row(
                node.get("node_id"),
                node.get("battery"),
                node.get("temperature"),
                node.get("health"),
                Text(finding, style=finding_style)
            )
        
        return Panel(table, title=f"ALERM: {swarm_status['alert_level']}")

    def generate_log_panel(self, logs):
        log_text = Text()
        for log in logs[-15:]:  # Son 15 log
            log_text.append(f"[{time.strftime('%H:%M:%S')}] {log}\n", style="dim")
        
        return Panel(log_text, title="Canlı Görev Logları")

    def render_mission(self, nodes_data, swarm_status, logs):
        self.layout["header"].update(self.generate_header())
        self.layout["status"].update(self.generate_status_table(nodes_data, swarm_status))
        self.layout["logs"].update(self.generate_log_panel(logs))
        self.layout["footer"].update(Panel(Text(f"Adaptif Mod: {swarm_status['adaptive_mode']} | Konsensüs: AKTİF", justify="center")))
        
        self.console.clear()
        self.console.print(self.layout)

if __name__ == "__main__":
    # Test
    dm = DashboardManager()
    test_node = [{"node_id": "A-01", "battery": "%90", "temperature": "25C", "health": "NOMİNAL", "is_positive": False}]
    test_swarm = {"alert_level": "NOMİNAL", "adaptive_mode": False}
    dm.render_mission(test_node, test_swarm, ["Misyon başlatıldı", "Düğümler çevrimiçi"])
