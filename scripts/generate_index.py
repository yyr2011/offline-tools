import os

tools_dir = "tools"
output_file = "index.html"

# 配置每个工具的标题（可自定义）
tool_titles = {
    "base-converter.html": "Base Converter",
    "timestamp-converter.html": "Timestamp Converter",
    "world-time.html": "World Time",
    "regex-tester.html": "Regex Tester"
}

tools = [f for f in os.listdir(tools_dir) if f.endswith(".html")]
tools.sort()

# 生成美观 HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write("""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Offline Tools</title>
<style>
body { font-family: Arial, sans-serif; background: #f5f5f5; margin:0; padding:0; }
header { background: #4CAF50; color: white; padding: 20px; text-align: center; }
h1 { margin:0; font-size: 2rem; }
.container { display: flex; flex-wrap: wrap; justify-content: center; padding: 20px; gap: 20px; }
.card { background: white; padding: 15px; border-radius: 10px; width: 200px; box-shadow: 0 2px 6px rgba(0,0,0,0.2); text-align: center; text-decoration: none; color: #333; transition: transform 0.2s, box-shadow 0.2s; }
.card:hover { transform: translateY(-5px); box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
.card h2 { margin: 10px 0; font-size: 1.2rem; }
</style>
</head>
<body>
<header>
<h1>Offline Tools</h1>
<p>All your handy offline utilities in one place</p>
</header>
<div class="container">
""")
    for tool in tools:
        title = tool_titles.get(tool, tool.replace(".html","").replace("-", " ").title())
        f.write(f'  <a class="card" href="{tools_dir}/{tool}"><h2>{title}</h2></a>\n')

    f.write("""</div>
</body>
</html>""")