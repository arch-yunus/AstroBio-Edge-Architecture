import json
import os
import time

class ReportGenerator:
    def __init__(self, log_path=None):
        self.log_path = log_path or "logs/mission_events.json"
        self.output_path = "logs/mission_dashboard.html"

    def generate_html_report(self, data=None):
        """
        Görev verilerini görselleştiren modern bir HTML dashboard üretir.
        """
        if data is None:
            if not os.path.exists(self.log_path):
                print("[ReportGenerator] Hata: Log dosyası bulunamadı.")
                return
            with open(self.log_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

        # Eğer data bir liste değilse (BaseStation'dan gelen sözlük ise) düzelt
        events = data if isinstance(data, list) else data.get("detailed_findings", [])

        html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>AstroBio-Edge | Görev Kontrol Paneli</title>
    <style>
        :root {{ --bg: #0f172a; --card: #1e293b; --text: #f8fafc; --accent: #3b82f6; --success: #22c55e; --error: #ef4444; --warning: #f59e0b; }}
        body {{ font-family: 'Inter', system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 40px; line-height: 1.6; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .header {{ border-bottom: 2px solid #334155; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center; }}
        .card {{ background: var(--card); padding: 25px; border-radius: 12px; margin-bottom: 20px; border-left: 6px solid var(--accent); transition: transform 0.2s; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }}
        .card:hover {{ transform: translateY(-3px); }}
        .positive {{ border-left-color: var(--success); }}
        .negative {{ border-left-color: var(--error); }}
        .warning {{ border-left-color: var(--warning); }}
        .badge {{ padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; }}
        .badge-pos {{ background: var(--success); color: white; }}
        .badge-neg {{ background: #475569; color: white; }}
        .stat-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin-top: 15px; }}
        .stat-item {{ background: rgba(255,255,255,0.05); padding: 10px; border-radius: 6px; }}
        .stat-label {{ display: block; font-size: 0.75rem; color: #94a3b8; text-transform: uppercase; }}
        .stat-value {{ font-size: 1.1rem; font-weight: bold; }}
        h1 {{ color: #60a5fa; margin: 0; }}
        .timestamp {{ color: #94a3b8; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>🌌 AstroBio-Edge Architecture</h1>
                <p>Universal Class Edge Computing Node Coordination</p>
            </div>
            <div style="text-align: right;">
                <span class="badge" style="background:var(--accent)">MİSYON AKTİF</span><br>
                <small class="timestamp">Üretim: {time.strftime('%Y-%m-%d %H:%M:%S')}</small>
            </div>
        </div>
        
        <div class="content">
            {"".join([f'''
            <div class="card {"positive" if e.get('is_positive') else "negative"}">
                <div style="display: flex; justify-content: space-between;">
                    <strong>Düğüm: {e.get('node_id', 'Unknown')}</strong>
                    <span class="badge {"badge-pos" if e.get('is_positive') else "badge-neg"}">
                        {"POZİTİF BULGU" if e.get('is_positive') else "NOMİNAL"}
                    </span>
                </div>
                
                <div class="stat-grid">
                    <div class="stat-item"><span class="stat-label">Sağlık</span><span class="stat-value">{e.get('health', 'NOMİNAL')}</span></div>
                    <div class="stat-item"><span class="stat-label">Sıcaklık</span><span class="stat-value">{e.get('temperature', '---')}</span></div>
                    <div class="stat-item"><span class="stat-label">Batarya</span><span class="stat-value">{e.get('battery', '---')}</span></div>
                    <div class="stat-item"><span class="stat-label">Güven Oranı</span><span class="stat-value">%{e.get('confidence', 0)*100:.1f}</span></div>
                </div>

                <div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #334155;">
                    <small style="color: #94a3b8;">Detaylı Bulgular:</small><br>
                    <code style="color: #60a5fa;">{json.dumps(e.get('findings', {}), ensure_ascii=False)}</code>
                </div>
            </div>
            ''' for e in events[::-1]])}
        </div>
    </div>
</body>
</html>
        """
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"[ReportGenerator] Görev Dashboard'u başarıyla güncellendi: {self.output_path}")

def generate_final_report(data):
    gen = ReportGenerator()
    gen.generate_html_report(data)

if __name__ == "__main__":
    # Test için örnek veri
    test_data = [
        {"node_id": "TEST-01", "is_positive": True, "confidence": 0.85, "health": "NOMİNAL", "temperature": "25.0C", "battery": "%85", "findings": {"Amino": "Var"}}
    ]
    generate_final_report(test_data)
