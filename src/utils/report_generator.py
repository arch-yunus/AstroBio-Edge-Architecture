import json
import os

class ReportGenerator:
    def __init__(self, log_path="logs/discovery_events.json"):
        self.log_path = log_path
        self.output_path = "logs/mission_dashboard.html"

    def generate_html_report(self):
        if not os.path.exists(self.log_path):
            print("[ReportGenerator] Hata: Log dosyası bulunamadı.")
            return

        with open(self.log_path, 'r') as f:
            data = json.load(f)

        html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>AstroBio-Edge Görev Paneli</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; padding: 20px; }}
        .header {{ border-bottom: 2px solid #334155; padding-bottom: 10px; margin-bottom: 20px; }}
        .card {{ background: #1e293b; padding: 15px; border-radius: 8px; margin-bottom: 15px; border-left: 5px solid #3b82f6; }}
        .positive {{ border-left-color: #22c55e; }}
        .negative {{ border-left-color: #ef4444; }}
        .stat {{ font-weight: bold; color: #94a3b8; }}
        h1 {{ color: #60a5fa; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🌌 AstroBio-Edge Görev Kontrol Paneli</h1>
        <p>Gezegen: Mars | Görev: Keşif v1.0</p>
    </div>
    <div class="content">
        {"".join([f'''
        <div class="card {"positive" if e['is_positive'] else "negative"}">
            <strong>Düğüm ID: {e['node_id']}</strong><br>
            <span class="stat">Zaman:</span> {e['timestamp']}<br>
            <span class="stat">Sinyal/Gürültü Oranı (SNR):</span> {e['snr']:.2f}<br>
            <span class="stat">Güven Oranı:</span> {e['confidence']:.2f}<br>
            <span class="stat">Sonuç:</span> {"TESPİT EDİLDİ" if e['is_positive'] else "Nominal"}<br>
            <hr style="border: 0.5px solid #334155;">
            <small>Bulgular: {json.dumps(e['findings'])}</small>
        </div>
        ''' for e in data[::-1]])}
    </div>
</body>
</html>
        """
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[ReportGenerator] Görev Paneli üretildi: {self.output_path}")

if __name__ == "__main__":
    gen = ReportGenerator()
    gen.generate_html_report()
