# Track1 Day22 — Monetization & GTM Lab
**Nguyễn Văn An · 2A202602776 · Ngày: 08/10/2026**

---

## Sản phẩm: VinFast Dealer AI Booking Agent

> AI Agent thay nhân viên trực điện thoại CSKH — tự động xử lý lịch bảo dưỡng xe VinFast 24/7 cho hệ thống đại lý qua Zalo OA và Facebook Messenger.

---

## Cấu trúc bài nộp

| File | Nội dung |
|------|---------|
| [`NguyenVanAn_Day22_model.md`](./NguyenVanAn_Day22_model.md) | Monetization Model — 5 tab đầy đủ (thay thế file Excel, format markdown) |
| [`NguyenVanAn_Day22_onepager.md`](./NguyenVanAn_Day22_onepager.md) | Monetization One-Pager — 3 khối: Pricing, GTM, Evidence |
| [`NguyenVanAn_Day22_AI_critique_log.md`](./NguyenVanAn_Day22_AI_critique_log.md) | AI Critique Log — Prompt 4.7.1 + 4.7.3, Accept/Reject/Partial |
| [`NguyenVanAn_Day22_checklist.md`](./NguyenVanAn_Day22_checklist.md) | Final Checklist — 10 mục self-check |

---

## Tóm tắt kết quả (5 con số bắt buộc)

| Chỉ số | Giá trị |
|--------|---------|
| Cost/Job (biến phí) | **$0,210 = 5.334₫** |
| Giá sàn (3× Cost/Job) | **$0,630 = 16.000₫** |
| Giá bán đề xuất | **35.000₫/booking** + phí nền 1.500.000₫/tháng |
| Gross Margin (biến phí, không overhead) | **84,8%** ✅ |
| Gross Margin (pilot, 1 đại lý) | **12,2%** ⚠️ → cần 6+ đại lý để ≥ 60% |
| Value Metric | **Hybrid** (phí nền + per outcome) |
| Kênh GTM | **Partner-Led** (VinFast Vietnam Aftersales Division) |

---

## Điểm khác biệt so với bạn cùng đề tài (2A202602746)

| Khía cạnh | Lưu Xuân Dũng (2A202602746) | Nguyễn Văn An (2A202602776) |
|-----------|---------------------------|---------------------------|
| LLM | Gemini 2.5 Flash (⏳ giá khuyến mại) | Claude Haiku 4.5 (giá stable, không ⏳) |
| Scale | 3 xưởng nhỏ, 300 job/tháng | 1 đại lý trung bình, 500 job/tháng |
| Phân khúc | Xưởng độc lập | Đại lý ủy quyền VinFast |
| Kênh | Founder-led → Partner VinFast | Partner-Led VinFast (ưu tiên ngay) |
| Biến sinh tử | Containment rate | Số đại lý (breakeven = 6 đại lý) |
| Infra đặc thù | ChromaDB | Supabase pgvector + SMS Brandname |
| Pain moment | Ca trực buổi tối | Thứ 7 sáng peak hour |
| HITL cost | $0,0144/job | $0,08625/job (cao hơn vì fix prompt drift) |

---

## Ngày kiểm tra giá API

- **Claude Haiku 4.5:** 08/10/2026 — [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- **SMS Zalo Brandname:** 08/10/2026 — 600₫/SMS (gói < 10.000 SMS/tháng)
- **Supabase:** 08/10/2026 — $25/tháng (Pro plan)
- **Tỷ giá:** 25.400₫/USD (Vietcombank, 08/10/2026)
