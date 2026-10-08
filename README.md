# Track1 Day22 — Monetization & GTM Lab
**Học viên:** Nguyễn Văn An · **Mã số:** 2A202602776 · **Ngày thực hiện:** 08/10/2026

---

## 🚗 Sản phẩm: VinFast Dealer AI Booking Agent

> **AI Agent thay nhân viên trực điện thoại CSKH** — tự động xử lý lịch bảo dưỡng xe VinFast 24/7 cho hệ thống đại lý ủy quyền qua Zalo OA và Facebook Messenger, tích hợp trực tiếp qua API với hệ thống quản trị đại lý (DMS).

---

## 📁 Cấu trúc bài nộp đầy đủ

| File | Định dạng | Nội dung chi tiết |
|------|-----------|-------------------|
| [`NguyenVanAn_Day22_model.xlsx`](./NguyenVanAn_Day22_model.xlsx) | Excel (.xlsx) | **File mô hình tài chính chính thức** — điền đầy đủ cả 6 tab theo đúng chuẩn template `Day22-AI-Product-GTM-Monetization-Model.xlsx`. Mọi công thức tự động tính toán, đèn kiểm tra đạt chuẩn xanh. |
| [`NguyenVanAn_Day22_onepager.docx`](./NguyenVanAn_Day22_onepager.docx) | Word (.docx) | **One-Pager chính thức dạng Word** — hoàn thiện từ template `Day22-AI-Product-GTM-One-Pager-Template.docx` với đủ 3 khối: Pricing, GTM, Evidence Pack. |
| [`NguyenVanAn_Day22_onepager.pdf`](./NguyenVanAn_Day22_onepager.pdf) | PDF (.pdf) | **File One-Pager bản in PDF** chuẩn, xuất trực tiếp từ Microsoft Word. |
| [`Day22-AI-Product-GTM-Monetization-Model.xlsx`](./Day22-AI-Product-GTM-Monetization-Model.xlsx) | Excel (.xlsx) | File template gốc đã được điền đầy đủ số liệu thực chiến. |
| [`Day22-AI-Product-GTM-One-Pager-Template.docx`](./Day22-AI-Product-GTM-One-Pager-Template.docx) | Word (.docx) | File Word template gốc đã được điền đầy đủ nội dung. |
| [`NguyenVanAn_Day22_model.md`](./NguyenVanAn_Day22_model.md) | Markdown | Bản thuyết minh chi tiết 5 tab mô hình tài chính, công thức, giải trình kỹ thuật. |
| [`NguyenVanAn_Day22_onepager.md`](./NguyenVanAn_Day22_onepager.md) | Markdown | Bản One-Pager dạng văn bản Markdown chuẩn GitHub. |
| [`NguyenVanAn_Day22_onepager.html`](./NguyenVanAn_Day22_onepager.html) | HTML | Bản trình bày web đẹp mắt, responsive, hỗ trợ in ấn. |
| [`NguyenVanAn_Day22_AI_critique_log.md`](./NguyenVanAn_Day22_AI_critique_log.md) | Markdown | Nhật ký chạy AI Critique với Prompt 4.7.1 (Cost/Job Stress Test) & Prompt 4.7.3 (Channel Reality Check), ghi rõ các quyết định Accept / Reject / Partial. |
| [`NguyenVanAn_Day22_checklist.md`](./NguyenVanAn_Day22_checklist.md) | Markdown | Bảng tự kiểm tra 10 mục bắt buộc theo Rubric chấm điểm của Lab Day 22. |

---

## 📊 Tóm tắt 5 con số cốt lõi

| Chỉ số | Giá trị | Cơ sở / Công thức | Trạng thái |
|--------|---------|-------------------|------------|
| **Cost/Job (biến phí)** | **$0,210 = 5.334₫** | LLM API ($0,018) + Infra ($0,105) + Retry ($0,001) + HITL QA ($0,086) chia cho mẫu số 400 job completed | ✅ Hợp lý, đủ 5 thành phần |
| **Giá sàn (3× Cost/Job)** | **$0,630 = 16.000₫** | 3 × $0,210 theo quy tắc an toàn biên lợi nhuận gộp | ✅ Đạt chuẩn sàn |
| **Giá bán đề xuất** | **35.000₫/booking** + phí nền 1.500.000₫/tháng | Neo giữa lương nhân sự CSKH (12tr/tháng) và giá trị tạo thêm (100tr doanh thu xưởng/tháng) | ✅ Nằm trong vùng neo giá |
| **Gross Margin biến phí** | **84,8%** | $(1,378 - 0,210) / 1,378 = 84,76\%$ | ✅ An toàn (vùng 60% – 85%) |
| **Breakeven Containment** | **30,5%** | $R \ge (v+q+e)/(P \times (1-GM)+e)$ | ✅ Đạt (Containment hiện tại là 80% > 30,5%) |
| **Breakeven số đại lý** | **6 đại lý** | Để biên lợi nhuận gộp toàn phần (tính cả Overhead $400/tháng) đạt $\ge 60\%$ | 🎯 Kế hoạch scale trong 90 ngày |
| **Value Metric** | **Hybrid** | Phí nền 1.500.000₫/tháng + 20.000₫/booking confirmed | ✅ Attribution 9/10, Autonomy 9/10 |
| **Kênh GTM 90 ngày** | **Partner-Led** | VinFast Vietnam (Bộ phận Dịch vụ Hậu mãi & Mạng lưới Đại lý - Aftersales) | ✅ CAC Inside Sales ($32k) lệch 8,4× |

---

## 🔍 Điểm khác biệt so với bài tham khảo cùng đề tài (2A202602746 - Lưu Xuân Dũng)

| Khía cạnh | Bài tham khảo (Lưu Xuân Dũng - 2A202602746) | Bài làm thực chiến (Nguyễn Văn An - 2A202602776) |
|-----------|---------------------------------------------|--------------------------------------------------|
| **Mô hình LLM** | Gemini 2.5 Flash (đánh dấu ⏳ giá khuyến mại) | Claude Haiku 4.5 (giá stable chính thức, không có dấu ⏳) |
| **Quy mô mục tiêu** | 3 xưởng sửa chữa nhỏ, 300 job/tháng | Hệ thống đại lý ủy quyền VinFast 3S, 500 job thử / 400 job confirmed/tháng |
| **Phân khúc khách hàng** | Xưởng dịch vụ độc lập ngoài chuỗi | Đại lý ủy quyền chính hãng VinFast (Authorized 3S/1S Dealerships) |
| **Chiến lược kênh GTM** | Bán trực tiếp Founder-Led rồi mới tìm đối tác | Tập trung chọn duy nhất kênh **Partner-Led** qua khối Hậu mãi VinFast ngay từ đầu |
| **Biến sinh tử** | Containment rate | Số lượng đại lý onboard (ngưỡng hòa vốn 6 đại lý để hấp thụ chi phí cố định) |
| **Hạ tầng công nghệ** | ChromaDB local | Supabase pgvector + SMS Brandname gateway kết nối 2 chiều qua DMS API |
| **Pain moment** | Ca trực buổi tối vắng người | Thứ 7 khung giờ cao điểm (08h30 - 10h30) hotline và Zalo OA bị nghẽn |
| **Độ phủ chi phí HITL** | $0,0144/job (chỉ review sơ bộ) | $0,08625/job (tính đủ cả QA review 5% ca mẫu và chi phí kỹ sư tuning prompt drift) |

---

## 📅 Bằng chứng giá API (Cập nhật ngày 08/10/2026)

- **Claude Haiku 4.5 (Anthropic):** Input $1,00/1M token, Output $5,00/1M token, Cache Write $1,25/1M, Cache Read $0,10/1M — Nguồn: [platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- **SMS Zalo Brandname:** 600₫/SMS (gói dịch vụ doanh nghiệp)
- **Supabase pgvector (Pro Plan):** $25,00/tháng
- **Railway Server:** $5,00/tháng
- **Tỷ giá chuyển đổi:** 25.400 ₫/USD (Vietcombank công bố ngày 08/10/2026)
