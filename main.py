from fastapi import FastAPI
from pydantic import BaseModel
import cs2inspect

app = FastAPI()

class Sticker(BaseModel):
    slot: int
    sticker_id: int
    wear: float
    offset_x: float | None = None
    offset_y: float | None = None
    rotation: float | None = None

class Item(BaseModel):
    defindex: int
    paintindex: int
    paintseed: int
    paintwear: float
    rarity: int
    stickers: list[Sticker] = []

@app.post("/build_inspect")
def build_inspect(item: Item):
    b = cs2inspect.Builder(
        defindex=item.defindex,
        paintindex=item.paintindex,
        paintseed=item.paintseed,
        paintwear=item.paintwear,
        rarity=item.rarity,
    )

    for s in item.stickers:
        b.stickers.append(s.dict())

    pb = b.build()
    return {"inspect_link": cs2inspect.link(pb)}
