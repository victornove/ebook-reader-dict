from scripts_utils import get_soup

url = "https://fr.wiktionary.org/wiki/Mod%C3%A8le:Temps_g%C3%A9ologiques?action=edit"
soup = get_soup(url)

textarea = soup.find(id="wpTextbox1")
times = {}
for line in textarea.text.split("\n"):
    line = line.strip()
    if not line.startswith("|"):
        continue
    k, v = line[1:].split("=", 1)
    times[k] = v


print("times = {")
for t, r in sorted(times.items()):
    print(f'    "{t}": "{r}",')
print(f"}}  # {len(times):,}")
