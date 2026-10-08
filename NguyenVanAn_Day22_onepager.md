# MONETIZATION ONE-PAGER
## VinFast Dealer AI Booking Agent
### Nguyễn Văn An · 2A202602776 · Track1 Day22 · 08/10/2026

---

## 🎯 BẠN BÁN GÌ, CHO AI

**Sản phẩm:** AI Agent thay nhân viên trực điện thoại CSKH — tự động xử lý lịch bảo dưỡng xe VinFast 24/7 qua Zalo OA và Facebook Messenger của đại lý.

**Khách hàng:** Đại lý ủy quyền VinFast quy mô vừa (50–200 xe dịch vụ/tháng). Người ký duyệt: Giám đốc Vận hành hoặc Trưởng bộ phận CSKH.

**Ngân sách khách:** Nhân sự / Vận hành — khách so sánh với lương 1–2 nhân viên trực điện thoại (8–12 triệu₫/tháng), không với ngân sách phần mềm IT.

**1 Job được định nghĩa là:**
> 1 lịch bảo dưỡng được xác nhận thành công (`booking.status = CONFIRMED`), khách nhận SMS xác nhận, đại lý ghi nhận vào lịch kỹ thuật viên — mà không cần nhân viên CSKH can thiệp.

---

## 💰 KHỐI 1 — PRICING

### Cost/Job (biến phí, Biến thể A — bán phần mềm)

| Thành phần | Chi phí/job completed | Ghi chú |
|-----------|----------------------|---------|
| LLM API (Claude Haiku 4.5) | $0,01796 = 456₫ | Giá kiểm tra 08/10/2026; có cache → tiết kiệm 39,5% |
| Infra (Supabase + SMS + Railway + DMS) | $0,10450 = 2.654₫ | SMS 600₫/tin là chi phí lớn nhất |
| Retry (7%) | $0,00125 = 32₫ | API timeout ~3% + lỗi slot đầy ~4% |
| HITL QA nội bộ (5% ca, Biến thể A) | $0,08625 = 2.191₫ | Nhân viên CSKH đại lý tự xử lý ca escalate |
| **Subtotal biến phí** | **$0,210 = 5.334₫** | |
| Overhead (R&D + founder sales) | $1,000 = 25.400₫ | Amortize theo số đại lý |
| **Total với overhead (1 đại lý)** | **$1,210 = 30.734₫** | |

### Vùng giá bán

```
[Giá sàn: 16.000₫/booking] ──── [GIÁ ĐỀ XUẤT: 35.000₫] ──── [Giá trần: 50.000₫]
   = 3 × Cost/Job biến phí         neo theo lương nhân viên      = giá trị tạo ra 3%
```

**Cấu trúc giá (Hybrid):**
- **Phí nền:** 1.500.000₫/tháng/đại lý (không giới hạn user, không giới hạn kênh)
- **Phần outcome:** 20.000₫/booking confirmed
- **ARPU điển hình** (500 job thử, CR 80%): 1.500.000 + 400 × 20.000 = **9.500.000₫/tháng**

**Tại sao 35.000₫?**
Lương nhân viên CSKH: 8.000.000₫/tháng. Xử lý ~400 ca/tháng = 20.000₫/ca. Tổng cost of labor (lương + BHXH + thưởng + đào tạo) = 12–15 triệu₫/tháng → 30.000–37.500₫/ca. AI ở 35.000₫ rẻ hơn tổng cost of labor, hoạt động 24/7, không nghỉ phép.

### Gross Margin

| Scenario | GM% | Điều kiện |
|----------|-----|-----------|
| Biến phí (không overhead) | **84,8%** ✅ | Tại bất kỳ scale nào |
| Pilot (1 đại lý, có overhead) | **12,2%** ⚠️ | Cần scale |
| Mục tiêu (6+ đại lý) | **≥ 60%** 🎯 | Overhead amortize trên 6 đại lý |

### Breakeven

| Chỉ số | Giá trị |
|--------|---------|
| Breakeven containment (biến phí) | **9,4%** (rất thấp — model khỏe) |
| Breakeven số đại lý (GM ≥ 60%) | **6 đại lý** |
| Containment eval hiện tại | 80% (smoke test 50 ca) |

> **Biến sinh tử của mô hình:** Không phải containment rate, mà là tốc độ onboard đủ 6 đại lý để amortize overhead R&D.

---

## 🚀 KHỐI 2 — GO-TO-MARKET

### Value Metric đã chốt: **HYBRID**

Attribution Score: **19/25** (cao) — `booking.status = CONFIRMED` với flag `created_by: ai_agent` trong DB.
Autonomy Score: **20/25** (cao) — 80% job tự hoàn thành, 0 bước manual trong happy path.

**Lý do Hybrid thay vì Outcome thuần:** Thị trường đại lý VN cần thấy phí cố định để budget planning. Phí nền 1.500.000₫ < lương 1 ngày nhân viên, dễ duyệt qua bộ phận tài chính.

Benchmark: Intercom Fin ([fin.ai/pricing](https://fin.ai/pricing/)) = $0,99/resolution; Salesforce Agentforce ([salesforce.com/agentforce/pricing](https://www.salesforce.com/agentforce/pricing/)) = $0,10/action.

---

### Kênh phân phối: **Partner-Led (VinFast Vietnam)**

**Tại sao không Sales-Led:**

| Chỉ số | Giá trị |
|--------|---------|
| Ngân sách CAC | **$3.807/khách** (= $374 × 84,8% × 12 tháng) |
| ACV/năm | $4.488 |
| Deal/AE/ngày | 0,46 ✅ (số học khả thi) |
| CAC thực tế Sales-Led | **$32.000** ($8.000/opportunity ÷ 25% win rate) |
| Lệch | **8,4× ngân sách** ❌ |

**Partner được chọn:** VinFast Vietnam — Aftersales Division (400+ đại lý toàn quốc)
**Trạng thái:** Có connection qua VinFast Startup Collaboration 2026
**Giá trị cho VinFast:** Chuẩn hóa SLA booking trên toàn dealer network, đo booking-to-service rate tự động
**CAC ước tính với Partner-Led:** $500–1.500 (trong ngân sách $3.807 ✅)

---

### Pain Moment

> **"Thứ 7, 8h30 sáng** — nhân viên CSKH đại lý đang xử lý 3 cuộc gọi cùng lúc, 2 khách đang nhắn trên **Zalo OA** hỏi slot bảo dưỡng tuần tới — không trả lời kịp, khách bỏ qua đại lý khác. Nhân viên đang vừa nghe máy vừa mở **DMS** tra lịch kỹ thuật viên."

**Điểm nhúng:** Zalo OA chatbot + Facebook Messenger bot — nhúng trực tiếp vào kênh chat đại lý đang dùng, kết nối API với DMS để check slot realtime. Không bắt đại lý mở thêm tab mới.

---

### 90-Day Plan

| Tháng | Mục tiêu | Actions | KPI |
|-------|----------|---------|-----|
| **1 — Học** | 2 đại lý, vận hành tận tay | Deploy 2 đại lý (founder-led, độc lập với VinFast); ngồi với CSKH 2 buổi/tuần; thu 200 ca thật | 200 ca, CR ≥ 75%, 0 complaint nghiêm trọng |
| **2–3 — Đòn bẩy** | 5 đại lý qua Partner-Led | Xuất Pilot Report → VinFast Corporate; demo tại Dealer Conference Q4/2026; onboard 3 đại lý mới | 5 đại lý, 2.000 job/tháng |
| **4+ — Mở rộng** | Chỉ sau khi thắng VinFast | Expand Toyota/Honda SAU KHI 10 đại lý VinFast stable (NPS > 40, churn < 5%) | 10+ đại lý, MRR ≥ $3.740 |

---

## 📋 KHỐI 3 — EVIDENCE PACK

| Tài sản | Có gì | Thiếu gì | Deadline |
|---------|-------|----------|----------|
| **Eval Results** | Smoke test 50 ca: CR 78% (40/50 confirmed tự động) | Pilot 200 ca thật; formal eval bộ 50 test cases | Cuối Tháng 1 |
| **Procurement Q&A** | Chưa có văn bản chính thức | (1) AI hallucinate? → eval + fallback human; (2) Data bị train? → Anthropic không train trên API; (3) Startup chết? → Supabase export; (4) DMS integration fail? → fallback manual, booking vẫn không bị mất | Tháng 2 — trước gặp VinFast |
| **Pilot Report** | Template sẵn | 6 tuần × 200 ca: CR%, thời gian xử lý, booking thêm nhờ 24/7, % tiết kiệm thời gian nhân viên | Cuối Tháng 1 |

**Lý do Procurement cần Evidence Pack:**
Khi gặp VinFast Corporate, Procurement sẽ hỏi: "AI này hallucinate không? Data đại lý có bị train không?" — và founder không có mặt để trả lời lần sau. Evidence Pack là câu trả lời bằng văn bản, giúp deal đi qua phòng mua hàng.

---

## ✅ TÓM TẮT — BÀI TEST NGƯỜI LẠ (2 phút)

| Câu hỏi | Trả lời (≤ 1 câu) |
|---------|-------------------|
| Bạn bán gì? | AI tự động xử lý lịch bảo dưỡng xe VinFast 24/7 thay nhân viên CSKH đại lý |
| Cho ai? | Đại lý VinFast quy mô vừa, người ký duyệt là Giám đốc Vận hành |
| Tính tiền thế nào? | Hybrid: 1,5 triệu₫/tháng + 20.000₫/booking confirmed |
| Có lãi trên mỗi đơn vị không? | GM biến phí 84,8%; cần 6 đại lý để GM tổng ≥ 60% |
| Tiếp cận khách qua đâu? | Partner-Led VinFast Vietnam — 400+ đại lý trong network, CAC $500–1.500 vs budget $3.807 |

---

*Mọi con số trong One-Pager đều truy được về file `NguyenVanAn_Day22_model.md`.*
*Giá API kiểm tra ngày 08/10/2026 — Claude Haiku 4.5 là giá stable (không có dấu ⏳).*
