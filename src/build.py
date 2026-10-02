"""Собирает сайт: src/hero.html + блоки -> index.html (для GitHub Pages) и src/preview.html (для превью)."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

# (название, вес/объём, цена, фото или None, состав/примечание или None)
MENU = [
    ("hookah", "Кальяны", [
        ("Кальян Классический", "", "1 600", "hookah-classic", None),
        ("Кальян Премиум", "", "2 000", "hookah-premium", None),
        ("Кальян на любом фрукте", "", "+1 000", "hookah-fruit", "Чаша из фрукта, плюс к цене любого кальяна"),
    ]),
    ("snacks", "Закуски", [
        ("Креветки темпура", "120/40 г", "620", "tempura", None),
        ("Брускетта с лососем", "200 г", "590", "bruschetta", None),
        ("Брускетта с говядиной и пармезаном", "200 г", "620", None, None),
        ("Брускетта с вялеными томатами", "200 г", "490", None, None),
        ("Чесночные гренки", "80/40 г", None, None, None),
        ("Сырные палочки", "110/40 г", None, None, None),
    ]),
    ("salads", "Салаты", [
        ("Цезарь с курицей", "280 г", "590", "caesar", None),
        ("Салат с говядиной", "240 г", "720", None, None),
        ("Цезарь с креветками", "260 г", "620", None, None),
        ("Греческий салат", "280 г", "590", None, None),
        ("Салат с хрустящими баклажанами", "370 г", "690", None, None),
        ("Салат Деревенский", "220 г", "490", None, None),
    ]),
    ("soups", "Супы", [
        ("Борщ с говядиной", "280 г", "550", "borsch", None),
        ("Куриный суп", "260 г", "490", None, None),
        ("Том Ям с морепродуктами", "320 г", "690", None, None),
    ]),
    ("hot", "Горячее", [
        ("Свиные рёбра", "250-270 г", "720", "ribs", None),
        ("ВОК с курицей", "290 г", "590", "wok", None),
        ("Спагетти Карбонара", "190 г", "620", "carbonara", None),
        ("Куриная грудка", "260 г", "620", "chicken", "Со свежими овощами"),
        ("Бифштекс", "280 г", "690", None, "С картофельным пюре"),
        ("ВОК с креветками", "290 г", "620", None, None),
        ("Паста с лососем и креветками", "190 г", "690", None, None),
        ("Паста с курицей и беконом", "190 г", "670", None, None),
        ("Паста с курицей и грибами", "190 г", "550", None, None),
        ("Куриные котлеты", "230 г", "550", None, None),
        ("Пельмени со сметаной", "260 г", "620", None, None),
        ("Рваная говядина", "100 г", "870", None, None),
    ]),
    ("pizza", "Пицца", [
        ("Пеперони", "280 г", "590", "pizza-pesto", None),
        ("4 сыра", "260 г", "590", "pizza-cheese", None),
        ("Чикен Песто", "280 г", "590", None, None),
    ]),
    ("street", "Стрит-фуд", [
        ("Бургер с говядиной", "360 г", "720", "burger", "С картофелем фри"),
        ("Бургер с рваной говядиной", "420 г", "870", None, "С картофелем фри"),
        ("Бургер с курицей", "360 г", "620", None, "С картофелем фри"),
        ("Кесадилья с курицей", "360 г", "590", None, "С картофелем фри"),
        ("Сэндвич с курицей", "290 г", "490", None, None),
    ]),
    ("japan", "Японская кухня", [
        ("Поке с лососем", "260 г", "620", "poke", None),
        ("Филадельфия с лососем", "210 г", "690", None, None),
        ("Темпура ролл с креветками", "190 г", "620", None, None),
        ("Темпура ролл с лососем", "190 г", "620", None, None),
        ("Запечённый ролл с лососем", "220 г", "590", None, None),
        ("Запечённый ролл с курицей", "230 г", "450", None, None),
    ]),
    ("desserts", "Десерты", [
        ("Пахлава фисташковая", "", "490", "baklava", None),
        ("Шоколадный фондан с мороженым", "", "540", "fondant", None),
        ("Чизкейк Нью-Йорк", "", "350", None, None),
        ("Мороженое", "3 шарика", "190", None, None),
    ]),
    ("tea", "Чай", [
        ("Фирменный чай", "800 мл", "690", None, "Облепиховый, малина с имбирём, пуэр на вишне, витаминный"),
        ("Чёрный", "800 мл", "460", None, "Ассам, эрл грей"),
        ("Зелёный", "800 мл", "460", None, "Жасминовый, сенча"),
        ("Травяной и фруктовый", "800 мл", "460", None, "Бодрость, лесной сбор, гречишный, вишнёвый пунш"),
        ("Улун", "800 мл", "460", None, "Габа алишань, те гуань инь, да хун пао"),
        ("Пуэр", "800 мл", "460", None, "Шу пуэр «Лао Ча Тоу 20 лет»"),
    ]),
    ("drinks", "Напитки", [
        ("Домашний лимонад", "400 мл", "420", None, "Киви, яблоко-базилик, ананас-клюква, малина-огурец, манго-маракуйя, груша-апельсин"),
        ("Домашний лимонад", "1 л", "690", None, "Те же вкусы, кувшин на компанию"),
        ("Кола", "330 мл", "290", None, None),
        ("Вода с газом или без", "", "290", None, None),
        ("Сок", "300 мл", "250", None, None),
        ("Red Bull", "355 мл", "390", None, None),
    ]),
    ("beer", "Пиво", [
        ("Шпатен", "450 мл", "490", None, "Светлый лагер, 5,2%"),
        ("Корона Экстра", "330 мл", "490", None, "Светлый лагер, 4,5%"),
        ("Пауланер", "500 мл", "550", None, "Пшеничное нефильтрованное, 5,5%"),
        ("Францисканер", "450 мл", "490", None, "Светлое нефильтрованное, 5,0%"),
        ("Гиннесс Стаут", "500 мл", "550", None, "Тёмное, 4,2%"),
        ("Сидр Белый Феникс", "450 мл", "490", None, "5,6%"),
    ]),
]

MENU_CSS = """
/* Menu: horizontally scrollable category pills, photo cards for dishes with photos, compact two-column list for the rest */
.menu { padding-block: clamp(56px, 8vw, 104px); border-top: 1px solid var(--line); }
.section-title { font-family: var(--font-display); font-weight: 400; font-size: clamp(2.6rem, 6vw, 4.2rem); line-height: 1; margin: 0 0 12px; }
.section-note { color: var(--muted); margin: 0 0 32px; max-width: 60ch; }
.lunch { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px 24px; padding: 18px 22px; margin: 0 0 32px; border: 1.5px solid var(--accent); border-radius: var(--radius); }
.lunch p { margin: 0; min-width: 0; }
.lunch b { color: var(--accent); }
.lunch .price { font-family: var(--font-display); font-size: 2rem; line-height: 1; color: var(--accent); white-space: nowrap; }
.tabs { display: flex; gap: 8px; overflow-x: auto; scrollbar-width: none; margin: 0 0 32px; padding-bottom: 4px; -webkit-overflow-scrolling: touch; }
.tabs::-webkit-scrollbar { display: none; }
.tab { flex: none; min-height: 42px; padding: 0 18px; border-radius: 999px; border: 1.5px solid var(--line); background: transparent; color: var(--muted); font: 500 .95rem var(--font-body); cursor: pointer; transition: color .2s, border-color .2s, background-color .2s; }
.tab:hover { color: var(--fg); border-color: var(--muted); }
.tab[aria-selected="true"] { background: var(--fg); border-color: var(--fg); color: var(--bg); }
.tab:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.panel h3 { font-family: var(--font-display); font-weight: 400; font-size: 1.8rem; margin: 0 0 20px; }
.js .panel h3 { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
.panel + .panel { margin-top: 48px; }
.js .panel + .panel { margin-top: 0; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 230px), 1fr)); gap: 20px; margin: 0 0 32px; }
.card { min-width: 0; }
.card img { display: block; width: 100%; height: auto; aspect-ratio: 1; object-fit: cover; border-radius: var(--radius); background: var(--surface); }
.card-body { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; padding-top: 12px; }
.dish { margin: 0; font-weight: 700; min-width: 0; }
.meta { color: var(--muted); font-size: .88rem; font-weight: 400; }
.cost { white-space: nowrap; font-weight: 700; font-variant-numeric: tabular-nums; color: var(--accent); }
.list { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px 56px; margin: 0; padding: 0; list-style: none; }
.list li { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; min-width: 0; }
.list .dish { font-weight: 500; }
.list .meta { display: block; }
@media (max-width: 700px) { .list { grid-template-columns: 1fr; } .cards { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; } .card-body { flex-direction: column; gap: 4px; } }
"""

TABS_JS = """
<script>
(function () {
  var tabs = document.querySelectorAll('.tab');
  var panels = document.querySelectorAll('.panel');
  if (!tabs.length) return;
  document.documentElement.classList.add('js');
  function show(id) {
    tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.target === id ? 'true' : 'false'); t.tabIndex = t.dataset.target === id ? 0 : -1; });
    panels.forEach(function (p) { p.hidden = p.id !== id; });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { show(t.dataset.target); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      var n = tabs[(i + d + tabs.length) % tabs.length];
      n.focus(); show(n.dataset.target);
    });
  });
  show(tabs[0].dataset.target);
})();
</script>
"""


def price(p):
    return f"{escape(p)} ₽" if p else "уточняйте"


def meta(weight, note):
    bits = [b for b in (weight, (note[0].lower() + note[1:]) if (note and weight) else note) if b]
    return f'<span class="meta">{escape(", ".join(bits))}</span>' if bits else ""


def menu_html():
    tabs, panels = [], []
    for key, title, items in MENU:
        tabs.append(f'<button class="tab" role="tab" type="button" data-target="m-{key}" aria-controls="m-{key}">{escape(title)}</button>')
        cards = [i for i in items if i[3]]
        rest = [i for i in items if not i[3]]
        out = [f'<div class="panel" id="m-{key}" role="tabpanel"><h3>{escape(title)}</h3>']
        if cards:
            out.append('<div class="cards">')
            for name, w, p, img, note in cards:
                out.append(
                    f'<article class="card"><img src="img/menu/{img}.webp" width="640" height="640" loading="lazy" alt="{escape(name)}">'
                    f'<div class="card-body"><p class="dish">{escape(name)} {meta(w, note)}</p><span class="cost">{price(p)}</span></div></article>'
                )
            out.append("</div>")
        if rest:
            out.append('<ul class="list">')
            for name, w, p, _, note in rest:
                out.append(f'<li><p class="dish">{escape(name)} {meta(w, note)}</p><span class="cost">{price(p)}</span></li>')
            out.append("</ul>")
        out.append("</div>")
        panels.append("".join(out))
    return f"""
  <section class="menu" id="menu">
    <div class="wrap">
      <h2 class="section-title">Меню</h2>
      <p class="section-note">Кальяны, кухня и бар. Цены в рублях, актуальные цены уточняйте у официанта.</p>
      <div class="lunch" id="hookah">
        <p><b>Бизнес-ланч с кальяном</b> по будням с 12:00 до 16:30: суп, салат, горячее, чай или кофе и премиум-кальян.</p>
        <span class="price">990 ₽</span>
      </div>
      <div class="tabs" role="tablist" aria-label="Разделы меню">{''.join(tabs)}</div>
      {''.join(panels)}
    </div>
  </section>
"""


def main():
    page = (SRC / "hero.html").read_text(encoding="utf-8")
    page = page.replace("</style>", MENU_CSS + "</style>", 1)
    page = page.replace("</main>", menu_html() + "</main>\n" + TABS_JS, 1)
    (SRC / "preview.html").write_text(page, encoding="utf-8")
    head, body = page.split("</style>", 1)
    full = (
        '<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f"{head}</style>\n</head>\n<body>{body}</body>\n</html>\n"
    )
    (ROOT / "index.html").write_text(full, encoding="utf-8")


if __name__ == "__main__":
    main()
