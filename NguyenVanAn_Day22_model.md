# NguyenVanAn_Day22_model — Monetization Model
# Người thực hiện: Nguyễn Văn An (2A202602776)
# Ngày kiểm tra giá API: 08/10/2026
# Sản phẩm: VinFast Dealer AI Booking Agent — AI Agent tự động xử lý lịch bảo dưỡng xe cho hệ thống đại lý VinFast

---

## TAB 0 — README / QUY ƯỚC

| Mục | Nội dung |
|-----|---------|
| Ngày chốt giá | 08/10/2026 |
| Tỷ giá USD/VND | 25.400 ₫/USD (Vietcombank, 08/10/2026) |
| Mô hình LLM chính | Claude Haiku 4.5 (Anthropic) |
| Thứ tự làm | Tab 1 → Tab 3 → Tab 2 → Tab 4 → Tab 5 |
| Ghi chú | Mọi con số giá API phải ghi ngày kiểm tra. Giá đánh dấu ⏳ là giá khuyến mại có hạn. |

---

## TAB 1 — COST/JOB (Tab nặng nhất)

### S1 — Định nghĩa Job

**Định nghĩa 1 job:**
> 1 lịch bảo dưỡng được xác nhận thành công — tức là hệ thống tạo được booking với trạng thái `CONFIRMED`, khách nhận được SMS xác nhận, và đại lý đã ghi nhận vào lịch kỹ thuật viên — mà không cần nhân viên CSKH can thiệp.

**Câu định vị chọn:**
> **Phiên bản B:** "Thay nhân viên trực điện thoại CSKH xử lý lịch bảo dưỡng xe VinFast 24/7 cho hệ thống đại lý"

**Ngân sách:** Nhân sự / Vận hành (không phải ngân sách phần mềm IT)
**Người ký duyệt:** Giám đốc Vận hành hoặc Trưởng bộ phận CSKH của đại lý
**Câu hỏi khách tự đặt:** "Rẻ hơn lương 1–2 nhân viên trực điện thoại không?"

**Kiểm tra 3 câu:**
- [x] Khách coi là giá trị? → Có — booking confirmed = doanh thu dịch vụ cho đại lý
- [x] Đếm được tự động? → Có — query `booking.status = CONFIRMED` trong DB
- [x] Định nghĩa chặt? → Có — phải có SMS xác nhận và ghi lịch kỹ thuật viên, không chỉ bot trả lời

---

### S2 — Khối lượng

| Chỉ số | Giá trị | Ghi chú |
|--------|---------|---------|
| Số job thử / tháng | 500 | Ước tính từ quy mô 1 đại lý trung bình (150–200 xe/tháng, 30–40% đặt lịch qua điện thoại/chat) |
| Containment rate (CR) | 80% | Smoke test nội bộ trên 50 ca: 40 confirmed tự động, 10 escalate sang người |
| Job hoàn thành / tháng | **400** | 500 × 80% |
| Job escalate (không tính doanh thu) | 100 | 500 × 20% |
| Ghi chú eval | Containment 80% là ước tính từ smoke test 50 ca — cần chạy pilot thật 200+ ca để xác nhận |

---

### S3 — Chi phí LLM (Claude Haiku 4.5)

**Giá API (kiểm tra ngày 08/10/2026 tại https://platform.claude.com/docs/en/about-claude/pricing):**

| Model | Input | Output | Cache Write | Cache Read |
|-------|-------|--------|-------------|------------|
| Claude Haiku 4.5 | $1,00/1M token | $5,00/1M token | $1,25/1M token | $0,10/1M token |

**Cấu trúc 1 cuộc hội thoại (1 job):**
- Số lượt hội thoại: 5 lượt (khách cung cấp thông tin xe, chọn dịch vụ, chọn ngày, xác nhận, nhận booking)
- Token input / lượt: 3.500 token (gồm 2.800 system prompt + RAG bảng giá dịch vụ VinFast = cache được; 700 là input của khách)
- Token output / lượt: 250 token
- Cache write: 1 lần / session (lượt đầu tiên)
- Cache read: 4 lượt sau

**Tính chi phí LLM cho 1 job:**

| Khoản | Phép tính | Chi phí (USD) |
|-------|-----------|---------------|
| Cache write (lượt 1) | 2.800 token x $1,25/1M | $0,00350 |
| Cache read (4 lượt sau) | 4 × 2.800 × $0,10/1M | $0,00112 |
| Input fresh (5 lượt × 700 token) | 3.500 × $1,00/1M | $0,00350 |
| Output (5 lượt × 250 token) | 1.250 × $5,00/1M | $0,00625 |
| **Tổng LLM có cache** | | **$0,01437** |
| Tổng nếu KHÔNG cache | (5×3.500)×$1/1M + 1.250×$5/1M | $0,02375 |
| **Tiết kiệm nhờ cache** | | **~39,5%** |

> Booking cần phản hồi realtime → không dùng Batch API. Nếu có workflow phân tích xe sắp đến hạn (scheduled job) thì có thể batch (−50%) — ước tính 15% workload.

---

### S4 — Speech (Không áp dụng)

> Sản phẩm xử lý qua chat text (Facebook Messenger, Zalo OA, Website widget) — không có STT/TTS.

---

### S5 — Infra

| Thành phần | Chi phí / tháng | Chi phí / job completed (chia 400) |
|-----------|----------------|-------------------------------------|
| Vector DB (Supabase pgvector, $25/tháng) | $25,00 | $0,0625 |
| Embedding re-index (2 lần/tháng, ~100K token, $0,10/1M) | $0,02 | $0,000050 |
| Logging & monitoring (Better Stack free tier cho pilot) | $0,00 | $0,00 |
| SMS gateway (500 SMS × 600d = 300.000d = $11,81) | $11,81 | $0,02953 |
| Server (Railway.app Hobby $5/tháng) | $5,00 | $0,01250 |
| **Tổng Infra** | **$41,83** | **$0,10450** |

> **Ghi chú:** SMS là chi phí lớn nhất trong Infra — bắt buộc vì khách expect nhận SMS xác nhận. Khi scale, đàm phán gói bulk 300d/SMS.

**Infra corrected (chia cho 400 job completed nhưng chi phí phát sinh cho 500 job thử):**
- Vector DB + Server: chi phí cố định/tháng → chia cho 400 job completed = $0,0750
- SMS: chỉ gửi khi CONFIRMED = 400 SMS → $11,81/400 = $0,02953 (đã đúng)
- **Tổng Infra/job completed: $0,10450**

---

### S6 — Retry

| Chỉ số | Giá trị | Ghi chú |
|--------|---------|---------|
| % job phải retry | 7% | API timeout Anthropic ~3%, lỗi logic booking (slot hết) phải hỏi lại ~4% |
| Chi phí retry / tháng | 500 × 7% × $0,01437 = $0,50 | 35 job retry, mỗi job tốn thêm 1 lượt LLM |
| Chi phí retry / job completed | $0,50 / 400 = $0,00125 | |

---

### S7 — HITL

**Lựa chọn: Biến thể A — Bán phần mềm**

**Lý do:** Tôi bán SaaS cho đại lý, không bán kết quả managed. 100 ca escalate/tháng do nhân viên CSKH của đại lý xử lý. Chi phí nhân sự đó là của đại lý.

**HITL nội bộ (QA):**

| Loại | Tỷ lệ | Thời gian | Chi phí/giờ | Chi phí/tháng |
|------|-------|-----------|-------------|---------------|
| QA review edge cases | 5% job completed = 20 ca | 3 phút/ca | $4,50/giờ | 20 × 0,05h × $4,50 = $4,50 |
| Fix prompt drift | 1 lần/tuần × 30 phút | — | $15/giờ (dev) | $30/tháng |
| **Tổng HITL QA** | | | | **$34,50** |
| **HITL QA / job completed** | | | | **$34,50/400 = $0,08625** |

---

### S8 — Overhead

| Khoản | Chi phí/tháng |
|-------|--------------|
| R&D (1 dev × 20% thời gian, $1.000/tháng) | $200 |
| Sales (founder-led, 10h/tháng × $20/h) | $200 |
| **Tổng Overhead/tháng** | **$400** |
| **Overhead/job completed** | **$400/400 = $1,000** |

---

### TỔNG HỢP COST/JOB

| Thành phần | $/job completed | VND/job |
|-----------|-----------------|---------|
| LLM API (corrected: 500 sessions / 400 completed) | $0,01437 × (500/400) = $0,01796 | 456d |
| Infra | $0,10450 | 2.654d |
| Retry | $0,00125 | 32d |
| HITL QA | $0,08625 | 2.191d |
| **Subtotal biến phí** | **$0,210** | **5.334d** |
| Overhead | $1,000 | 25.400d |
| **TOTAL với Overhead** | **$1,210** | **30.734d** |

---

## TAB 2 — PRICING

### Giá sàn và giá bán

| Chỉ số | Tính toán | Kết quả |
|--------|-----------|---------|
| Cost/Job biến phí | Tab 1 | $0,210 = 5.334d |
| **Giá sàn (3× biến phí)** | $0,210 × 3 | $0,630 = **16.000d** |
| **Giá bán đề xuất** | Neo theo lương | **35.000d/booking ($1,378)** |
| **ARPU Hybrid/tháng** | 1.500.000d phí nền + 400×20.000d | **9.500.000d ($374)** |
| GM (tại scale, không overhead) | (35.000 - 5.334) / 35.000 | **84,8%** |
| GM (pilot, với overhead) | (35.000 - 30.734) / 35.000 | **12,2%** ⚠️ |

> **Giải thích GM thấp ở pilot:** Overhead $400/tháng ($10.160.000d) amortize trên 400 job là $1/job. Khi scale 5 đại lý (2.000 job), overhead/job = $0,20, GM → 82%. **Kế hoạch scale đến 5 đại lý trong tháng 4–6.**

### Neo giá trần

| Cách neo | Tính toán | Kết quả |
|----------|-----------|---------|
| Neo theo lương nhân viên | Lương CSKH 8.000.000d/tháng, 400 ca = 20.000d/ca. Charge 50–70% = 10.000–14.000d | 12.000d |
| Neo theo giá trị | 125 booking thêm nhờ 24/7 × 800.000d ASP = 100tr/tháng. Charge 3% | 7.500d/booking |
| **Giá đề xuất** | Giữa hai neo, dễ khách kiểm chứng | **35.000d/booking** |

> **Tại sao 35.000d (cao hơn neo lương 20.000d):** Vì đại lý so với tổng chi phí nhân viên (lương + BHXH + thưởng + đào tạo) = 12–15 triệu/tháng → 30.000–37.500d/ca. AI ở 35.000d vẫn rẻ hơn tổng cost of labor.

### Stress Test

| CR | Job completed | Revenue/tháng | Biến phí | GM% (không OH) |
|----|---------------|---------------|----------|-----------------|
| 60% | 300 | 6.000.000d (fee) + 1.500.000d (nền) = 7.500.000d | 1.600.200d | 78,7% |
| 70% | 350 | 7.000.000d + 1.500.000d = 8.500.000d | 1.867.000d | 78% |
| **80%** | **400** | **8.000.000d + 1.500.000d = 9.500.000d** | **2.133.600d** | **77,5%** |
| 90% | 450 | 9.000.000d + 1.500.000d = 10.500.000d | 2.400.300d | 77,1% |

> **Nhận xét:** Phí nền 1.500.000d là buffer quan trọng — ngay cả khi CR = 60%, GM% vẫn >75%.

### Breakeven Volume

```
Để GM ≥ 60% (tính cả overhead, tại 1 đại lý):
Revenue - Biến phí - Overhead >= 60% × Revenue
(1.500.000 + 20.000×N) - 5.334×N - 10.160.000 >= 0,60 × (1.500.000 + 20.000×N)

Với N = số job completed:
1.500.000 + 20.000N - 5.334N - 10.160.000 >= 900.000 + 12.000N

(20.000 - 5.334 - 12.000)N >= 900.000 - 1.500.000 + 10.160.000
2.666N >= 9.560.000
N >= 3.587 job/tháng (1 đại lý)
```

> ⚠️ **Với 1 đại lý duy nhất:** breakeven GM 60% đòi hỏi 3.587 job/tháng — xa vời.
> 
> **Với 5 đại lý (overhead chia đều):** Overhead/đại lý = $80 ($2.032.000d). Breakeven = **281 job/tháng/đại lý** → khả thi.
>
> **Breakeven containment hiện tại:** Pilot 500 job × 80% = 400 job → đạt được nếu có 5 đại lý cùng lúc (400×5 = 2.000 job, xấp xỉ ngưỡng).

---

## TAB 3 — VALUE METRIC

### Attribution Score (5 câu × 5 điểm = 25)

| Câu hỏi | Điểm | Bằng chứng |
|---------|------|-----------|
| Đo được kết quả do AI tạo ra? | 5 | `booking.status = CONFIRMED` với `created_by: ai_agent` trong DB |
| Có log chứng minh AI (không phải human) tạo booking? | 5 | Session log đầy đủ, timestamp, không có human action trong flow |
| Có A/B test hoặc baseline so sánh? | 3 | Chưa có A/B test formal; có baseline lịch sử booking qua điện thoại trước khi deploy |
| Khách có thể tranh cãi kết quả không do AI? | 2 | Rất khó — flow confirmed = 0 human intervention |
| Có refund policy cho job không thành công? | 4 | Chỉ tính tiền booking CONFIRMED — escalate không tính |
| **Tổng Attribution** | **19/25** | **→ CAO** |

### Autonomy Score (5 câu × 5 điểm = 25)

| Câu hỏi | Điểm | Bằng chứng |
|---------|------|-----------|
| AI hoàn thành end-to-end không cần người? | 4 | 80% tự chạy xong; 20% escalate |
| Có human review trước khi tính completed? | 5 | Không — CONFIRMED = tự động |
| AI xử lý được edge cases phổ biến? | 3 | 5/7 loại edge case chính (đổi lịch, hủy, slot đầy, hỏi giá, xe mới) |
| Pipeline có bước manual trong flow chính? | 4 | 0 bước manual trong happy path |
| Ai trigger job? | 4 | Khách trigger → AI xử lý hoàn toàn |
| **Tổng Autonomy** | **20/25** | **→ CAO** |

**Attribution CAO + Autonomy CAO → GÓC: OUTCOME (hoặc Hybrid)**

### Benchmark

| Sản phẩm | Job tương tự | Value Metric | Giá | Link |
|---------|-------------|--------------|-----|------|
| Intercom Fin | 1 support ticket resolved | Outcome: $0,99/resolution | $0,99 | https://fin.ai/pricing/ |
| Salesforce Agentforce | 1 AI conversation | Hybrid: phí nền + per action | $5/user/tháng + $0,10/action | https://www.salesforce.com/agentforce/pricing/ |

### Value Metric đã chốt: **HYBRID**

- Phí nền: 1.500.000d/tháng/đại lý
- Phần outcome: 20.000d/booking confirmed
- ARPU điển hình: 9.500.000d/tháng

**Decision Note 3 câu:**

1. **Tôi chọn Hybrid** (1.500.000d nền + 20.000d/job) vì phí nền bảo vệ overhead cố định ngay từ đại lý đầu tiên, phần outcome scale theo giá trị thật.

2. **Attribution 19/25 (cao)** — đo được `booking.status = CONFIRMED` với flag `created_by: ai_agent`. **Autonomy 20/25 (cao)** — 80% job tự hoàn thành không qua human review. Bằng chứng: smoke test 50 ca.

3. **Market override sang Hybrid thay vì Outcome thuần:** Thị trường đại lý xe VN chưa quen "trả theo kết quả" — họ cần thấy phí cố định để budget planning. Phí nền 1.500.000d nhỏ hơn lương 1 nhân viên/ngày, dễ duyệt qua bộ phận tài chính.

---

## TAB 4 — CHANNEL FIT

### Thông số

| | Giá trị |
|-|---------|
| ARPU/tháng | $374 (9.500.000d) |
| ACV/năm | $4.488 |
| GM (tại scale) | 84,8% |
| Phân khúc | SMB (đại lý xe VinFast, doanh thu 5–50 tỷd/năm) |
| CAC Payback | < 12 tháng (SMB) |

### Ngân sách CAC

```
Ngân sách CAC = $374 × 84,8% × 12 = $3.807/khách
```

### Sales-Led Check

```
Số deal/AE/năm = $500.000 quota / $4.488 ACV = 111 deal/năm
Số deal/AE/ngày = 111 / 240 = 0,46 deal/ngày ✓ (<1, khả thi số học)

CAC thực tế = $8.000 (cost/opportunity) / 25% win rate = $32.000
Lệch = $32.000 / $3.807 = 8,4× ❌ → Sales-Led full cycle không khả thi
```

### Chấm điểm 3 kênh (1–5)

| Tiêu chí | PLG | Sales-Led | Partner-Led |
|----------|-----|-----------|-------------|
| Phù hợp ARPU | 2 | 3 | 4 |
| CAC trong ngân sách | 5 | 1 | 4 |
| Phù hợp pain moment | 2 | 4 | 5 |
| Scale với đội nhỏ | 3 | 2 | 4 |
| Tốc độ khách đầu tiên | 2 | 4 | 3 |
| Đòn bẩy quan hệ | 1 | 3 | 5 |
| **Tổng** | **15/30** | **17/30** | **25/30** |

### Kênh đã chốt: **Partner-Led**

- **Partner:** VinFast Vietnam — bộ phận After-Sales & Dealer Network (400+ đại lý toàn quốc)
- **Trạng thái liên hệ:** Đang chuẩn bị — có 1 connection qua chương trình VinFast Startup Collaboration 2026
- **Giá trị cho partner:** VinFast muốn chuẩn hóa chất lượng dịch vụ bảo dưỡng của toàn bộ dealer network — AI booking agent giúp đo được SLA, tỷ lệ booking-to-service, customer satisfaction tự động

**Kết quả:**
- Ngân sách CAC: **$3.807**
- Deal/AE/ngày: **0,46** (khả thi số học)
- CAC thực tế: **$32.000** → lệch **8,4×** → Sales-Led không khả thi
- Kênh đã chốt: **Partner-Led (VinFast Vietnam)**
- Tên partner: **VinFast Vietnam — Aftersales Division**
- Đã liên hệ chưa: **Qua chương trình VinFast Startup Collaboration 2026**

---

## TAB 5 — 90-DAY PLAN & EVIDENCE PACK

### Pain Moment

> **"Thứ 7, 8h30 sáng, nhân viên CSKH đại lý đang xử lý 3 cuộc gọi cùng lúc, 2 khách nhắn Zalo OA hỏi còn slot bảo dưỡng tuần tới không — nhân viên không trả lời kịp, khách bỏ qua đại lý khác. Lúc đó nhân viên đang vừa nghe điện thoại vừa mở phần mềm DMS (Dealer Management System) để tra lịch kỹ thuật viên."**

**Điểm nhúng:** Zalo OA chatbot + Facebook Messenger bot — nhúng trực tiếp vào kênh chat khách hàng đại lý, kết nối API với DMS để check slot thật.

### 90-Day Plan

| Giai đoạn | Thời gian | Mục tiêu | Actions | KPI | Người phụ trách |
|-----------|-----------|----------|---------|-----|-----------------|
| **Tháng 1 — Học** | Tuần 1–4 | 2 đại lý, vận hành tận tay | Deploy tại 2 đại lý quen biết; ngồi với nhân viên CSKH 2 buổi/tuần; thu thập 200 ca thật | 200 ca, CR ≥ 75%, 0 complaint nghiêm trọng | Nguyễn Văn An (founder) |
| **Tháng 2–3 — Đòn bẩy** | Tuần 5–12 | Mở rộng qua VinFast Partner | Xuất pilot report → gửi VinFast Corporate Aftersales; xin demo tại Dealer Conference Q4/2026; onboard 3 đại lý mới qua giới thiệu | 5 đại lý, 2.000 job/tháng, GM ≥ 60% | Nguyễn Văn An + 1 BD |
| **Tháng 4+ — Mở rộng** | Từ tháng 4 | Chỉ mở rộng sau khi thắng ngách VinFast | Expand sang Toyota/Honda dealer SAU KHI đạt 10 đại lý VinFast stable; dựa trên NPS > 40, churn < 5% | 10+ đại lý VinFast, MRR ≥ $3.740 | BD team |

### Evidence Pack

| Tài sản | Trạng thái | Nội dung / Deadline |
|---------|-----------|---------------------|
| **Eval Results** | 🟡 Một phần | Smoke test 50 ca: CR 78%. Cần pilot 200 ca thật. **Deadline: Cuối tháng 1** |
| **Procurement Q&A** | 🔴 Chưa có | 3 câu cần trả lời: (1) AI hallucinate? → có eval + fallback human; (2) Data có bị train? → Anthropic API policy không train; (3) Startup chết thì data đâu? → Supabase, export bất cứ lúc. **Deadline: Tháng 2 trước gặp VinFast** |
| **Pilot Report** | 🔴 Chưa có | 6 tuần, 200 ca, CR%, thời gian xử lý, booking thêm nhờ 24/7, % tiết kiệm thời gian nhân viên. **Deadline: Cuối tháng 1** |

---

## TỔNG KẾT — 5 CON SỐ BẮT BUỘC

| Chỉ số | Giá trị |
|--------|---------|
| **Cost/Job (biến phí)** | $0,210 = **5.334d** |
| **Giá sàn (3× biến phí)** | $0,630 = **16.000d** |
| **Giá bán đề xuất** | $1,378 = **35.000d/booking** + phí nền 1.500.000d/tháng |
| **Gross Margin (tại scale, không overhead)** | **84,8%** |
| **Gross Margin (pilot, với overhead đầy đủ)** | **12,2%** ⚠️ → cần 5+ đại lý để đạt 60%+ |
| **Breakeven volume** | 47 job/tháng (biến phí); 3.587 job/tháng (GM 60% với 1 đại lý) |
| **Breakeven containment** | 9,4% (cực thấp — model khỏe về biến phí) |
