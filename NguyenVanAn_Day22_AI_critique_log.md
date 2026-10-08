# AI Critique Log — Day22 Monetization Lab
# Người thực hiện: Nguyễn Văn An (2A202602776)
# Ngày: 08/10/2026
# Sản phẩm: VinFast Dealer AI Booking Agent
# Quy tắc: Accept (sửa theo) | Reject (giữ, có lý do) | Partial

═══════════════════════════════════════════════════════════════════
PROMPT 4.7.1 — COST/JOB STRESS TEST
[Đã chạy với Claude Sonnet 4.6 Thinking, 08/10/2026 23:30]
═══════════════════════════════════════════════════════════════════

INPUT gửi AI:
  Product: VinFast Dealer AI Booking Agent
  Job: 1 booking CONFIRMED (booking.status = CONFIRMED, SMS sent, lịch kỹ thuật viên ghi nhận)
  Volume: 500 job thử/tháng, containment 80% → 400 completed
  LLM: Claude Haiku 4.5, $1,00/$5,00 per 1M token, cache $1,25/$0,10
  Infra: Supabase $25 + SMS $11,81 + Railway $5 + embedding $0,02 = $41,83/tháng
  Retry: 7%, HITL QA 5% (Biến thể A - bán phần mềm)
  Overhead: $400/tháng (R&D + founder-led sales)

OUTPUT từ AI — tóm tắt & phản hồi:

1. MISSING COST CATEGORIES:

   AI: "Chi phí DMS API integration bị bỏ qua. Kết nối với Dealer Management
   System của từng đại lý thường có phí API hoặc middleware cost."
   → ACCEPT: Đúng. Mỗi đại lý dùng DMS khác nhau (VinFast Pro, Autosys, v.v.).
     Chi phí integration: ước tính $50-100 one-time + $10/tháng maintenance.
     Phân bổ: $10/tháng / 400 job = $0,025/job completed.
     ĐIỀU CHỈNH: Thêm vào Infra $10/tháng/đại lý.
   ✅ ACCEPT

   AI: "Chi phí monitoring/alerting thiếu. Không thể production mà không có
   uptime monitoring — đặc biệt với SMS gateway là critical path."
   → PARTIAL: Better Stack free tier đủ cho pilot 1-2 đại lý. Khi scale > 5 đại lý,
     cần nâng lên Better Stack Scale $29/tháng → phân bổ $5,80/đại lý/tháng = $0,0145/job.
   ✅ PARTIAL — thêm vào cost model khi scale qua 5 đại lý

   AI: "Bạn chưa tính cost of Zalo OA subscription. Zalo Official Account
   có phí hàng tháng cho doanh nghiệp."
   → ACCEPT: Đúng. Zalo OA Official (verified): ~500.000d/năm = 41.667d/tháng = ~$1,64/tháng.
     Phân bổ: $1,64 / 400 job = $0,0041/job. Nhỏ nhưng cần ghi nhận.
   ✅ ACCEPT

2. DENOMINATOR CHECK:

   AI: "Bạn đã điều chỉnh đúng — LLM cost phát sinh cho 500 sessions nhưng
   chỉ 400 job được tính doanh thu. Tỷ lệ hiệu chỉnh 500/400 = 1,25 là đúng.
   Kiểm tra: Infra cố định (Supabase, Railway) cũng cần chia cho 400, không phải 500."
   → ACCEPT: Đúng — Infra cố định đã được chia cho 400 job completed.
     Infra biến phí (SMS): chỉ gửi khi CONFIRMED = 400 SMS → đã chia đúng.
   ✅ ACCEPT — mẫu số đã đúng

   AI recomputed Cost/Job:
   - LLM: $0,01437 × (500/400) = $0,01796
   - Infra (cố định): $41,83/400 = $0,10457 (≈ $0,10450 — khớp)
   - Retry: $0,50/400 = $0,00125
   - HITL QA: $4,50+$30 = $34,50/400 = $0,08625
   - Subtotal biến phí: $0,210 ✓
   ✅ AI xác nhận tính toán đúng

3. TOKEN MATH AUDIT:

   AI: "Cache write 2.800 token lượt đầu, cache read 4 lượt sau × 2.800 = 11.200 token.
   Tính: 2.800×$1,25/1M + 11.200×$0,10/1M = $0,00350 + $0,00112 = $0,00462 — khớp.
   Output 5 lượt × 250 = 1.250 token × $5/1M = $0,00625 — khớp.
   Input fresh 5 lượt × 700 = 3.500 × $1/1M = $0,00350 — khớp.
   TỔNG: $0,01437 — đúng."
   → REJECT: AI đồng ý tính toán đúng — không cần sửa.

   AI: "Cache saving: ($0,02375 - $0,01437) / $0,02375 = 39,5% — đúng."
   → REJECT: Đã tính đúng.

   AI: "Batch API không khả thi cho booking realtime — đồng ý. Nhưng
   workflow cảnh báo xe sắp đến hạn bảo dưỡng (proactive outreach) CÓ THỂ
   dùng batch. Ước tính 15% workload → tiết kiệm 7,5% LLM tổng."
   → PARTIAL ACCEPT: Đúng về kỹ thuật. Ghi chú trong model cho future feature,
     chưa tính vào cost/job chính vì chưa implement.

4. PRICE VOLATILITY:

   AI: "Claude Haiku 4.5 giá $1/$5 per 1M là giá stable (không có dấu ⏳ trong
   Anthropic pricing page). Đây là giá list chính thức — ít rủi ro thay đổi
   trong 6 tháng tới so với các model đang trong giai đoạn early access."
   → ACCEPT: Điểm tốt. Lý do chọn Claude Haiku 4.5 thay vì Gemini Flash (⏳)
     là để tránh rủi ro price volatility. Decision này được confirm là đúng.
   ✅ ACCEPT — an toàn hơn Gemini Flash

   AI: "SMS gateway (Brandname Zalo) có thể thay đổi giá theo chính sách
   Zalo mà không báo trước. Cần ghi ngày kiểm tra giá SMS."
   → ACCEPT: Đúng. Ngày kiểm tra giá SMS Zalo Brandname: 08/10/2026.
     Giá: 600d/SMS, áp dụng cho gói < 10.000 SMS/tháng.
   ✅ ACCEPT

5. BREAKEVEN SENSITIVITY:

   AI recomputed:
   "Tại giá 35.000d/booking và phí nền 1.500.000d:
   
   GM ≥ 60% tại 1 đại lý (có overhead $400/tháng = 10.160.000d):
   (1.500.000 + 20.000N) - 5.334N - 10.160.000 >= 0,60 × (1.500.000 + 20.000N)
   
   Giải ra: N >= 3.587 job/tháng — như mô hình của bạn.
   
   Sensitivity table (1 đại lý, có overhead):
   - CR 50%: 250 job, Revenue 6.500.000d, Cost 11.493.500d, GM = -76,8% (lỗ)
   - CR 60%: 300 job, Revenue 7.500.000d, Cost 11.760.200d, GM = -56,8% (lỗ)
   - CR 70%: 350 job, Revenue 8.500.000d, Cost 12.027.000d, GM = -41,5% (lỗ)
   - CR 80%: 400 job, Revenue 9.500.000d, Cost 12.293.600d, GM = -29,4% (lỗ)
   - CR 90%: 450 job, Revenue 10.500.000d, Cost 12.560.300d, GM = -19,6% (lỗ)
   
   → Với 1 đại lý, KHÔNG THỂ đạt GM 60% dù CR = 100%.
   
   Với 5 đại lý (overhead chia 5 = $80/đại lý/tháng = 2.032.000d):
   - CR 80%: 400 job/đại lý, Revenue 9.500.000d, Cost 4.165.600d, GM = 56,2% (gần đạt)
   
   Với 6 đại lý (overhead = $67/đại lý = 1.693.333d):
   - CR 80%: GM = 60,1% ✅"
   → ACCEPT: AI đã phát hiện vấn đề quan trọng. Mô hình chỉ đạt GM 60% khi
     có ≥ 6 đại lý. Đây là biến sinh tử của mô hình, không phải containment rate.
   ✅ ACCEPT — Đã điều chỉnh phân tích trong model: "breakeven = 6 đại lý"

6. THE ONE NUMBER THAT KILLS ME:

   AI: "Biến duy nhất mà nếu sai 2x sẽ giết mô hình là: SỐ ĐẠI LÝ.
   
   Tại sao: Overhead $400/tháng là fixed. Với 1 đại lý, GM = -29% ngay cả
   ở CR 80%. Nếu bạn giả định 5 đại lý nhưng thực tế chỉ đạt 3 đại lý sau
   3 tháng (2× thấp hơn kế hoạch), GM vẫn âm (-8%).
   
   Không phải LLM cost, không phải SMS cost, không phải containment rate.
   Mà là khả năng onboard đủ số đại lý để amortize overhead R&D."
   → ACCEPT HOÀN TOÀN: Đây là insight quan trọng nhất của stress test.
     Kế hoạch 90 ngày phải ưu tiên số 1: onboard 6+ đại lý trước tháng 4.
     Evidence Pack và Partner-Led VinFast là chìa khóa để làm được điều này.
   ✅ ACCEPT — Đã ghi vào 90-Day Plan: "Tháng 2-3: 5 đại lý, GM ≥ 60% cần 6+"

═══════════════════════════════════════════════════════════════════
PROMPT 4.7.3 — CHANNEL REALITY CHECK
[Đã chạy với Claude Sonnet 4.6 Thinking, 08/10/2026 23:45]
═══════════════════════════════════════════════════════════════════

INPUT gửi AI:
  ARPU: $374/tháng, GM: 84,8%, Phân khúc: SMB
  CAC budget: $3.807/khách
  Kênh đã chọn: Partner-Led (VinFast Vietnam)
  Pain moment: Thứ 7, 8h30, nhân viên CSKH đại lý xử lý 3 cuộc gọi + 2 Zalo OA,
               khách bỏ qua vì không được trả lời. Đang dùng: Zalo OA + DMS.

OUTPUT từ AI — tóm tắt & phản hồi:

1. ACV CHECK:

   AI: "ACV = $374 × 12 = $4.488. Quota AE $500k → 111 deal/năm → 0,46/ngày.
   Con số 0,46 deal/ngày là khả thi về số học nhưng bạn cần cẩn thận:
   - ACV $4.488 là rất thấp cho inside sales. Tomasz Tunguz đặt ngưỡng ~$3.000 ACV
     để justify inside sales — bạn đang ở mức vừa đủ, không dư.
   - Founder-led tháng 1-3 là đúng. Sau đó mới cần xem xét có hire AE không.
   Kết luận: Sales-Led pure là không khả thi ($32k CAC vs $3.807 budget).
   Partner-Led là lựa chọn hợp lý."
   → ACCEPT: Đồng ý với kết luận. Founder-led + Partner-Led là con đường đúng.

2. CAC GAP:

   AI: "CAC thực tế $32.000 vs budget $3.807 = lệch 8,4×. Đây là gap cực lớn.
   Với Partner-Led VinFast, CAC có thể giảm xuống $500-1.500/khách:
   - $500 nếu VinFast tự giới thiệu và endorsement chính thức
   - $1.500 nếu bạn tự outreach từng đại lý trong network VinFast
   Cả hai đều trong ngân sách $3.807. Partner-Led solve được bài toán CAC."
   → ACCEPT: Đây là lý do cốt lõi chọn Partner-Led. Số cụ thể từ AI giúp
     defend lựa chọn kênh khi pitch với investor.
   ✅ ACCEPT

3. PAIN MOMENT STRESS TEST:

   AI: "Pain moment của bạn đủ cụ thể — có đủ 3 phần:
   - MẤY GIỜ: Thứ 7, 8h30 sáng ✓
   - ĐANG LÀM GÌ: xử lý 3 cuộc gọi + 2 Zalo OA cùng lúc ✓
   - DÙNG APP NÀO: Zalo OA + DMS ✓
   
   Điểm nhúng bạn đề xuất (Zalo OA chatbot + Messenger bot) là đúng.
   
   CHÚ Ý: Tích hợp với DMS là critical path — nếu không check được slot thật,
   bot sẽ confirm booking nhưng kỹ thuật viên không có slot → worst case.
   Đây là technical risk lớn nhất, không phải AI risk."
   → ACCEPT: AI đúng về DMS integration risk. Đây là điều cần ghi vào
     Procurement Q&A: 'Chúng tôi tích hợp với DMS của đại lý để check slot
     realtime — không confirm booking khi slot không có thật.'
   ✅ ACCEPT — DMS integration risk đã thêm vào Evidence Pack planning

4. PARTNER-LED INCENTIVE CHECK:

   AI: "Để Partner-Led VinFast work, cần đảm bảo 3 điều:
   1. VinFast có incentive gì? → Họ muốn chuẩn hóa trải nghiệm CSKH trên
      toàn dealer network. Mỗi booking missed = khách bỏ sang hãng khác.
      AI booking agent giúp VinFast đo SLA và tỷ lệ booking-to-service.
   2. VinFast có bị mất margin không? → Không. Đây là tool cho đại lý mua,
      không phải VinFast mua. VinFast chỉ cần endorsement, không tốn tiền.
   3. Fastest way to falsify: gặp 1 người trong bộ phận Aftersales VinFast
      trong 2 tuần. Nếu họ 'thú vị nhưng cần xin ý kiến cấp trên' → track
      slow. Nếu họ 'chúng tôi đang tìm giải pháp như thế này' → track fast."
   → ACCEPT: Breakdown 3 điều kiện rất rõ. Lần gặp đầu với VinFast cần
     bring số: pilot report từ 2 đại lý, eval results, booking missed reduction.
   ✅ ACCEPT

5. STRONGEST ARGUMENT AGAINST PARTNER-LED:

   AI: "Rủi ro lớn nhất của Partner-Led VinFast:
   VinFast có thể quyết định tự build hoặc mua giải pháp lớn hơn (FPT, VNPT)
   thay vì endorsement startup. Khi bạn phụ thuộc vào 1 partner duy nhất,
   mất partner = mất toàn bộ kênh.
   
   Mitigation:
   - Không chờ VinFast xong mới approach dealer. Song song: onboard 2 đại lý
     qua founder-led ngay tháng 1 — đây là fallback nếu VinFast chậm.
   - Khi có 6-10 đại lý dùng, bargaining power tăng — VinFast FOMO nếu không
     partner sớm vì sản phẩm đã chạy trong network của họ."
   → ACCEPT HOÀN TOÀN: Đây là feedback quan trọng nhất.
     Đã sửa 90-Day Plan: Tháng 1 là founder-led 2 đại lý — KHÔNG chờ VinFast.
     VinFast là kênh scale, không phải điều kiện bắt buộc để bắt đầu.
   ✅ ACCEPT — 90-Day Plan đã điều chỉnh

═══════════════════════════════════════════════════════════════════
TỔNG KẾT ACCEPT/REJECT/PARTIAL
═══════════════════════════════════════════════════════════════════

PROMPT 4.7.1 — 6 điểm:
  ✅ ACCEPT (4): DMS API cost, SMS ngày kiểm tra, Claude ổn định hơn Gemini Flash,
                  breakeven = số đại lý (not containment)
  ✅ PARTIAL (1): Monitoring cost khi scale > 5 đại lý
  ❌ REJECT (1): Token math — AI xác nhận đúng, không cần sửa

PROMPT 4.7.3 — 5 điểm:
  ✅ ACCEPT (4): ACV check, CAC gap với Partner-Led, DMS integration risk,
                  founder-led parallel với VinFast approach
  ✅ ACCEPT (1): Partner-Led risk mitigation → sửa 90-Day Plan

THAY ĐỔI ĐÃ ÁP DỤNG VÀO MODEL:
1. Thêm DMS API cost vào Infra: $10/tháng/đại lý
2. Thêm Zalo OA subscription: 41.667d/tháng
3. Breakeven analysis: cần 6 đại lý để GM ≥ 60%, không phải 5
4. 90-Day Plan Tháng 1: founder-led 2 đại lý — KHÔNG chờ VinFast
5. Evidence Pack: thêm DMS integration risk → Procurement Q&A câu 4
6. Ghi ngày kiểm tra giá SMS: 08/10/2026, 600d/SMS

ĐIỀU CHỈNH KHÔNG ÁP DỤNG (có lý do):
- Batch API cho proactive outreach: chưa implement feature này, không đưa vào
  cost model chính để tránh bias optimistic
- Monitoring cost: chưa tính vào model pilot, sẽ thêm khi scale > 5 đại lý
