"""
Script tạo file HTML từ One-Pager markdown
Nguyễn Văn An - Day22 Lab
"""
import markdown
import os

# Đọc file markdown
script_dir = os.path.dirname(os.path.abspath(__file__))
md_file = os.path.join(script_dir, "NguyenVanAn_Day22_onepager.md")
html_file = os.path.join(script_dir, "NguyenVanAn_Day22_onepager.html")

with open(md_file, "r", encoding="utf-8") as f:
    md_content = f.read()

# Convert markdown sang HTML
md = markdown.Markdown(extensions=["tables", "toc"])
html_body = md.convert(md_content)

# Template HTML với CSS đẹp
html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monetization One-Pager — VinFast Dealer AI Booking Agent</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            line-height: 1.6;
            color: #1a1a2e;
            background: #f8f9fa;
        }}
        
        .page {{
            max-width: 960px;
            margin: 0 auto;
            background: white;
            padding: 32px 40px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }}
        
        /* Header */
        h1 {{
            font-size: 22px;
            font-weight: 700;
            color: #0d47a1;
            border-bottom: 3px solid #1565c0;
            padding-bottom: 8px;
            margin-bottom: 4px;
        }}
        
        h2 {{
            font-size: 14px;
            font-weight: 600;
            color: #1565c0;
            margin-top: 20px;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        
        h2::before {{
            content: '';
            display: inline-block;
            width: 4px;
            height: 16px;
            background: #1565c0;
            border-radius: 2px;
            flex-shrink: 0;
        }}
        
        h3 {{
            font-size: 12px;
            font-weight: 600;
            color: #37474f;
            margin-top: 12px;
            margin-bottom: 6px;
        }}
        
        /* Tables */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 8px 0;
            font-size: 12px;
        }}
        
        th {{
            background: #1565c0;
            color: white;
            padding: 6px 10px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 5px 10px;
            border-bottom: 1px solid #e8eaf6;
        }}
        
        tr:nth-child(even) td {{
            background: #f3f4fd;
        }}
        
        tr:hover td {{
            background: #e8eaf6;
        }}
        
        /* Blockquotes */
        blockquote {{
            background: #e3f2fd;
            border-left: 4px solid #1565c0;
            padding: 10px 14px;
            margin: 8px 0;
            border-radius: 0 6px 6px 0;
            font-style: normal;
            color: #0d47a1;
        }}
        
        /* Code blocks */
        pre {{
            background: #1a1a2e;
            color: #a5d6a7;
            padding: 12px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 11px;
            font-family: 'Courier New', monospace;
            margin: 8px 0;
        }}
        
        code {{
            background: #e8eaf6;
            color: #1565c0;
            padding: 1px 5px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        
        pre code {{
            background: transparent;
            color: inherit;
            padding: 0;
        }}
        
        /* Links */
        a {{
            color: #1565c0;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        /* Paragraphs */
        p {{
            margin: 6px 0;
        }}
        
        /* Lists */
        ul, ol {{
            margin: 6px 0 6px 20px;
        }}
        
        li {{
            margin: 2px 0;
        }}
        
        /* HR */
        hr {{
            border: none;
            border-top: 1px solid #e8eaf6;
            margin: 16px 0;
        }}
        
        /* Special badges */
        .badge-pass {{
            display: inline-block;
            background: #4caf50;
            color: white;
            padding: 1px 6px;
            border-radius: 10px;
            font-size: 10px;
            font-weight: 600;
        }}
        
        /* Print styles */
        @media print {{
            body {{ background: white; }}
            .page {{ box-shadow: none; padding: 20px; }}
        }}
        
        /* Footer */
        .footer {{
            margin-top: 24px;
            padding-top: 12px;
            border-top: 1px solid #e8eaf6;
            font-size: 10px;
            color: #78909c;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="page">
        {html_body}
        <div class="footer">
            Nguyễn Văn An · 2A202602776 · Track1 Day22 · Ngày kiểm tra giá API: 08/10/2026 · 
            Tỷ giá: 25.400₫/USD (Vietcombank)
        </div>
    </div>
</body>
</html>"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"[OK] Da tao: {html_file}")
print(f"   File size: {os.path.getsize(html_file):,} bytes")
print("   Mo file HTML bang trinh duyet de xem hoac in thanh PDF (Ctrl+P -> Save as PDF)")
