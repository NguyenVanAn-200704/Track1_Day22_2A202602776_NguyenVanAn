# Final Checklist — Xác nhận hoàn thành Lab Day 22
# Người thực hiện: Nguyễn Văn An (2A202602776)
# Ngày: 08/10/2026 | Sản phẩm: VinFast Dealer AI Booking Agent

════════════════════════════════════════════════════════════════
SELF-CHECK — 10 MỤC BẮT BUỘC
════════════════════════════════════════════════════════════════

[✓]  1. Tab 1 — đủ 5 thành phần chi phí, không ô nào trống vô lý
     → API (LLM Claude Haiku 4.5): $0,01796/job completed ✅
     → Infra (Supabase + SMS + Railway + DMS API + Zalo OA): $0,10450/job ✅
     → Retry (7%): $0,00125/job ✅
     → HITL (QA nội bộ Biến thể A): $0,08625/job ✅
     → Overhead ($400/tháng): $1,000/job ✅
     → KHÔNG ô nào = 0 mà không có lý do ✅

[✓]  2. Tab 1 — mẫu số là JOB HOÀN THÀNH, không phải job thử
     → 500 job thử × 80% = 400 job confirmed ✅
     → LLM cost corrected: 500 sessions / 400 completed (×1,25) ✅
     → Infra cố định chia cho 400 completed ✅

[⚠️]  3. Tab 2 — Giá bán ≥ 3 × Cost/Job, Gross Margin ≥ 60%
     → Giá bán: 35.000d = $1,378/job ✅
     → 3 × Cost/Job biến phí: 3 × $0,210 = $0,630 = 15.993d ✅ (giá bán > giá sàn)
     → Gross Margin (không overhead): 84,8% ✅
     → Gross Margin (có overhead, 1 đại lý): 12,2% ❌
     → KẾ HOẠCH: Scale lên 6+ đại lý để GM ≥ 60% ✅
     → ĐÈN VÀNG (không phải đỏ) — GM biến phí đạt, GM tổng chưa đạt ở scale hiện tại
     → Không sửa số để đẹp — có kế hoạch cụ thể ✅

[✓]  4. Tab 2 — Breakeven containment đã tính, đã so với eval
     → Breakeven volume: ≥ 6 đại lý (400 job/đại lý, CR 80%) để GM ≥ 60% ✅
     → Eval hiện tại: CR 80% (smoke test 50 ca: 40 confirmed / 50 thử) ✅
     → Đã so sánh và ghi nhận: containment đủ, cần số đại lý ✅

[✓]  5. Tab 3 — Value Metric + Decision Note + 2 benchmark có link
     → Value Metric: Hybrid (1.500.000d/tháng + 20.000d/booking confirmed) ✅
     → Attribution Score: 19/25 (cao) ✅
     → Autonomy Score: 20/25 (cao) ✅
     → Decision Note: 3 câu đầy đủ ✅
     → Benchmark 1: Intercom Fin https://fin.ai/pricing/ ✅
     → Benchmark 2: Salesforce Agentforce https://www.salesforce.com/agentforce/pricing/ ✅

[✓]  6. Tab 4 — Ngân sách CAC, deal/AE/ngày, 1 kênh duy nhất
     → Ngân sách CAC: $3.807/khách (ARPU × GM × 12 tháng) ✅
     → Deal/AE/ngày: 0,46 deal/ngày ✅ (khả thi về số học, ACV $4.488)
     → CAC thực tế Sales-Led: $32.000 = 8,4× ngân sách → không khả thi ✅
     → 1 kênh chốt: Partner-Led (VinFast Vietnam Aftersales Division) ✅
     → Tên partner: VinFast Vietnam ✅
     → Trạng thái: Qua chương trình VinFast Startup Collaboration 2026 ✅

[✓]  7. Tab 5 — 90-day plan có số; Evidence Pack có deadline
     → Tháng 1: 2 đại lý, 200 ca, CR ≥ 75% ✅
     → Tháng 2-3: 5 đại lý, 2.000 job/tháng ✅
     → Evidence Pack: 3 tài sản, đều có deadline rõ ràng ✅

[✓]  8. Ghi ngày kiểm tra giá API ở tab 6_Benchmarks
     → Claude Haiku 4.5: kiểm tra 08/10/2026 tại platform.claude.com/docs/en/about-claude/pricing ✅
     → SMS Zalo Brandname: kiểm tra 08/10/2026, 600d/SMS ✅
     → Giá Claude không có dấu ⏳ (stable, không phải khuyến mại) ✅

[✓]  9. One-Pager — 3 khối, mọi số khớp Excel
     → Khối 1 Pricing: Cost/Job $0,210 = 5.334d, giá 35.000d, GM 84,8% ✅
     → Khối 2 GTM: Kênh Partner-Led VinFast, Pain Moment đủ 3 phần, 90-day plan ✅
     → Khối 3 Evidence: 3 tài sản có trạng thái và deadline ✅
     → Mọi số truy được về model ✅

[✓]  10. Đã chạy ít nhất 2 prompt ở §4.7 và ghi lại accept/reject
     → Prompt 4.7.1 Cost/Job Stress Test: ✅ (6 điểm, 4 Accept, 1 Partial, 1 Reject)
     → Prompt 4.7.3 Channel Reality Check: ✅ (5 điểm, 5 Accept)
     → Tất cả quyết định do tác giả viết lại bằng lời của mình ✅

════════════════════════════════════════════════════════════════
PASS/FAIL CHECKPOINTS CHI TIẾT
════════════════════════════════════════════════════════════════

Checkpoint 1 — Ngân sách & Job:
✅ Câu định vị nói công việc bị thay thế: "Thay nhân viên trực điện thoại CSKH"
✅ Nêu được ai ký duyệt: Giám đốc Vận hành / Trưởng CSKH đại lý
✅ Job định nghĩa theo giá trị và đếm được: booking.status = CONFIRMED (DB query)
✅ Ngân sách: Nhân sự / Vận hành

Checkpoint 2 — Value Metric:
✅ Khớp ma trận: Attribution CAO (19/25) + Autonomy CAO (20/25) → gợi ý Outcome/Hybrid
✅ Chọn Hybrid (không phải Outcome thuần) vì lý do thị trường rõ ràng
✅ Có 2 sản phẩm thật + link nguồn
⚠️ Không chọn Outcome thuần: CR 80% từ smoke test 50 ca — cần pilot 200+ ca để confirm

Checkpoint 3 — Cost/Job & Giá:
✅ Đủ 5 thành phần (API, Infra, HITL, Retry, Overhead)
✅ Mẫu số là job hoàn thành (400, không phải 500)
✅ GM biến phí 84,8% > 60%
✅ Ghi ngày kiểm tra giá API: 08/10/2026
✅ Breakeven volume đã tính và đối chiếu với eval
⚠️ GM full (với overhead, 1 đại lý): 12,2% — có kế hoạch scale rõ ràng

Checkpoint 4 — Kênh:
✅ Đúng 1 kênh cho 90 ngày: Partner-Led
✅ Có ngân sách CAC từ công thức: $3.807
✅ Có số deal/AE/ngày (0,46) và kết luận
✅ Partner-Led: có tên công ty (VinFast Vietnam) + trạng thái liên hệ

Checkpoint 5 — Pain Moment & Plan:
✅ Pain Moment đủ 3 phần: Thứ 7 8h30 + xử lý 3 cuộc gọi + 2 Zalo OA + Zalo OA/DMS
✅ Điểm nhúng cụ thể: Zalo OA chatbot + Facebook Messenger bot
✅ 90-day plan có số và người chịu trách nhiệm
✅ Tháng 1 là giai đoạn học (2 đại lý, 200 ca) — không phải scale

Checkpoint 6 — One-Pager:
✅ 3 khối đầy đủ
✅ Mọi số truy được về model
✅ Evidence Pack: có nội dung cụ thể và deadline rõ ràng
(Bài test người lạ: chưa test với nhóm khác — sẽ thực hiện trước khi nộp)

════════════════════════════════════════════════════════════════
LỖI ĐÃ PHÁT HIỆN VÀ SỬA (nhờ AI Critique)
════════════════════════════════════════════════════════════════

1. Thiếu DMS API integration cost → Đã thêm $10/tháng/đại lý vào Infra
2. Thiếu Zalo OA subscription cost → Đã thêm 41.667d/tháng
3. Phân tích breakeven không đủ → Đã tính: cần 6 đại lý (không phải 5)
4. 90-Day Plan phụ thuộc vào VinFast → Đã sửa: Tháng 1 founder-led độc lập

════════════════════════════════════════════════════════════════
ĐIỂM TỰ ĐÁNH GIÁ (theo Rubric)
════════════════════════════════════════════════════════════════

#1 Cost/Job Rigor (30đ): ~26/30
   → Đủ 5 thành phần, HITL và Retry không = 0, mẫu số đúng
   → Trừ: GM 12,2% tại pilot cần giải thích rõ hơn (đã có nhưng cần trình bày gọn hơn)

#2 Value Metric Justification (25đ): ~22/25
   → Có ma trận Attribution × Autonomy, Decision Note 3 câu, 2 benchmark + link
   → Trừ: Smoke test 50 ca chưa đủ để confirm Attribution — đã ghi rõ limitation

#3 Channel Evidence (20đ): ~18/20
   → Có ngân sách CAC ($3.807), deal/AE/ngày (0,46), CAC thực tế ($32k, lệch 8,4×)
   → Partner-Led có tên VinFast Vietnam + trạng thái liên hệ

#4 Pain Moment & 90-Day Plan (15đ): ~13/15
   → Pain Moment đủ 3 phần, điểm nhúng cụ thể, Tháng 1 là giai đoạn học

#5 Evidence Pack Readiness (10đ): ~8/10
   → 3 tài sản, thành thật về khoảng trống, có deadline rõ ràng

Tổng ước tính: ~87/100 → Strong band ✅
