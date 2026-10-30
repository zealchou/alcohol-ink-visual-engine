# 共用交接契約
以 JSON 保存一次任務的可檢查決策。所有盒子採整張畫布左上角為原點的 [x,y,width,height] 正規化座標，值介於 0–1；角色區域可重疊，但文字區不可被高密度紋理侵入。

```json
{
  "version": "1.0",
  "task_id": "campaign-001",
  "mode": "generate",
  "goal": "讓讀者理解三個覺察方法",
  "audience": "一般成人",
  "platform": "instagram",
  "canvas": {"width":1080,"height":1350,"pages":5},
  "brand": {"status":"provisional","colors":["#163A46","#E8EEE9"],"forbidden":[],"logo_asset":null},
  "style": {"primary":"silk-mist","secondary":null,"role":"accent","ink_strength":0.2,"texture_density":0.2,"metallic_ratio":0,"negative_space":0.65},
  "visual_lock": {"palette":"brand.colors","flow":"lower-left to upper-right","edge":"soft with local pigment rims","type_family":"available CJK sans","lighting":"soft","reference_assets":[]},
  "regions": {"subject":[0.6,0.1,0.35,0.8],"text":[0.08,0.12,0.48,0.72],"ink":[0,0.75,1,0.25]},
  "preserve": ["提供的人臉與商品標誌"],
  "skills": [{"role":"ink","name":"alcohol-ink-visual-engine","status":"available"}],
  "pages": [{"index":1,"purpose":"hook","headline":"先停一下，再決定","body":[],"cta":null}],
  "output": {"format":"PNG","transparency":false,"editable":false},
  "decision": {"reason":"低強度暈染支持安定感並保留閱讀空間","fallback":"quiet-space"},
  "authorization": {"publish":false,"schedule":false},
  "qa": {"status":"pending","issues":[]}
}
```
範例 pages 陣列僅示意第一頁；實際製作前必須補滿 canvas.pages，連號 1..N。
使用者要求可編輯成品時，實際建立可編輯圖層或模板，不能將合成 PNG 稱為可編輯；能力不足時說明。
跨工具交接只傳必要素材與契約，不傳與任務無關的個人記憶。
