import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import sys

sys.stdout.reconfigure(encoding='utf-8')

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def style_run(run, font_name="Calibri", size_pt=10, bold=False, italic=False, color_rgb=(0,0,0)):
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)

def build_docx():
    doc = docx.Document('Day22-AI-Product-GTM-One-Pager-Template.docx')
    
    # 1. Header paragraphs
    # P2: Tên / Nhóm & Sản phẩm
    p2 = doc.paragraphs[2]
    p2.text = ""
    r = p2.add_run("Tên / Nhóm: ")
    style_run(r, bold=True, size_pt=10.5)
    r = p2.add_run("Nguyễn Văn An (2A202602776)          ")
    style_run(r, bold=True, size_pt=10.5, color_rgb=(0, 51, 102))
    r = p2.add_run("Sản phẩm: ")
    style_run(r, bold=True, size_pt=10.5)
    r = p2.add_run("VinFast Dealer AI Booking Agent")
    style_run(r, bold=True, size_pt=10.5, color_rgb=(0, 51, 102))

    # P3: Value Metric & Kênh & Ngày
    p3 = doc.paragraphs[3]
    p3.text = ""
    r = p3.add_run("Value Metric đã chọn: ")
    style_run(r, bold=True, size_pt=10)
    r = p3.add_run("Hybrid (1,5tr nền + 20k/job)   ")
    style_run(r, bold=True, size_pt=10, color_rgb=(0, 102, 51))
    r = p3.add_run("Kênh đã chọn: ")
    style_run(r, bold=True, size_pt=10)
    r = p3.add_run("Partner-Led (VinFast)   ")
    style_run(r, bold=True, size_pt=10, color_rgb=(0, 102, 51))
    r = p3.add_run("Ngày: ")
    style_run(r, bold=True, size_pt=10)
    r = p3.add_run("08/10/2026")
    style_run(r, bold=True, size_pt=10, color_rgb=(102, 102, 102))

    # NGÂN SÁCH KHÁCH HÀNG (P8)
    p8 = doc.paragraphs[8]
    p8.text = "• Ngân sách: Nhân sự / Vận hành (CSKH & Điều phối dịch vụ xưởng). Người ký duyệt: Giám đốc Đại lý ủy quyền hoặc Trưởng phòng Dịch vụ sau bán hàng (Aftersales Service Manager).\n• Bối cảnh so sánh: Khách hàng so sánh chi phí phần mềm với chi phí tuyển thêm 1 nhân viên CSKH trực ca tối/cuối tuần (10–12 triệu VNĐ/tháng gồm lương, BHXH và quản lý). AI Agent giúp phủ kín 24/7 với chi phí chỉ bằng 79% lương 1 nhân sự và tạo thêm doanh thu bảo dưỡng."
    for r in p8.runs:
        style_run(r, size_pt=9.5)

    # VALUE METRIC + LÝ DO (P12)
    p12 = doc.paragraphs[12]
    p12.text = "• Lựa chọn: Mô hình HYBRID gồm Phí nền cố định 1.500.000 VNĐ/tháng/đại lý kết hợp 20.000 VNĐ/lịch bảo dưỡng xác nhận thành công (booking status = CONFIRMED).\n• Điểm số: Attribution đạt 9/10 (audit log gắn mã booking trên DMS, SMS Brandname gửi thành công) · Autonomy đạt 9/10 (AI tự động 80% quy trình 24/7 không cần người can thiệp theo smoke test 50 ca).\n• Lý do thị trường chọn Hybrid thay vì Outcome thuần: Thị trường đại lý ô tô tại Việt Nam yêu cầu tính ổn định trong lập dự toán ngân sách (predictable budget). Phí nền 1.500.000 VNĐ bảo đảm bù đắp 100% chi phí hạ tầng (Supabase, Railway server, webhook connector) ngay từ tháng đầu, trong khi phí 20.000 VNĐ/job gắn liền với giá trị gia tăng thực tế."
    for r in p12.runs:
        style_run(r, size_pt=9.5)

    # BENCHMARK — 2 SẢN PHẨM THẬT CÙNG LOẠI JOB (P17)
    p17 = doc.paragraphs[17]
    p17.text = "1. Intercom Fin: Value Metric: Outcome (Resolution) · Giá công bố: $0,99 / resolution · Link: https://fin.ai/pricing/\n2. Salesforce Agentforce: Value Metric: Hybrid (Platform fee + per Action) · Giá công bố: $5/user/tháng + $0,10/action · Link: https://salesforce.com/agentforce/pricing/"
    for r in p17.runs:
        style_run(r, size_pt=9.5)

    # TABLE 0: CÁC CON SỐ PRICING
    t0 = doc.tables[0]
    # Row 1: Cost/Job
    t0.rows[1].cells[1].text = "$0,210  (5.334 VNĐ)"
    # Row 2: Giá sàn
    t0.rows[2].cells[1].text = "$0,630  (16.000 VNĐ)"
    # Row 3: Giá bán đề xuất
    t0.rows[3].cells[1].text = "$1,378  (35.000 VNĐ) [hoặc 20k + 1,5tr nền]"
    # Row 4: Gross Margin
    t0.rows[4].cells[1].text = "84,8%  (An toàn ≥ 60%)"
    # Row 5: Breakeven containment
    t0.rows[5].cells[1].text = "30,5%  (Ngưỡng sống còn)"
    # Row 6: Containment hiện tại
    t0.rows[6].cells[1].text = "80,0%  (Đạt lành mạnh, > 30,5%)"

    for r_idx in range(1, len(t0.rows)):
        for c_idx in [0, 1, 2]:
            cell = t0.rows[r_idx].cells[c_idx]
            for p in cell.paragraphs:
                for r in p.runs:
                    style_run(r, size_pt=9, bold=(c_idx==1))

    # CÁCH NEO GIÁ (P23)
    p23 = doc.paragraphs[23]
    p23.text = "• Neo 2 đầu: (1) Neo theo giá trị tạo ra (9,5%): AI mang lại thêm trung bình 125 booking ngoài giờ/tháng × 800.000 VNĐ doanh thu trung bình = 100 triệu VNĐ doanh thu xưởng; mức thu 9.500.000 VNĐ/tháng tương đương 9,5% giá trị tạo ra (nằm trong vùng 10–25%).\n• (2) Neo theo lương nhân công (79%): Lương CSKH trực ca 12.000.000 VNĐ/tháng; mức phí 9.500.000 VNĐ tương đương 79% lương nhân sự nhưng hoạt động 24/7/365, không xin nghỉ phép, không bỏ lỡ khách hàng ban đêm."
    for r in p23.runs:
        style_run(r, size_pt=9.5)

    # MÔ HÌNH GÃY KHI NÀO? (P27)
    p27 = doc.paragraphs[27]
    p27.text = "Mô hình gãy khi containment rate tụt dưới 30,5% (Gross Margin tụt dưới 50% ở cấp độ biến phí) HOẶC số lượng đại lý dưới 3 đại lý (doanh thu không bù đắp được chi phí cố định R&D + QA $400/tháng)."
    for r in p27.runs:
        style_run(r, size_pt=9.5, bold=True, color_rgb=(153, 0, 0))

    # KÊNH PHÂN PHỐI (P32)
    p32 = doc.paragraphs[32]
    p32.text = "• Kênh duy nhất chọn cho 90 ngày đầu: PARTNER-LED.\n• Tên công ty đối tác: VinFast Vietnam — Bộ phận Dịch vụ Hậu mãi & Mạng lưới Đại lý (Aftersales & Dealer Network).\n• Trạng thái liên hệ: Đang tiếp cận thông qua chương trình VinFast Innovation Challenge / Vingroup Partner Network 2026.\n• Giá trị mang lại cho đối tác: Giúp VinFast chuẩn hóa quy trình tiếp nhận dịch vụ sau bán hàng của toàn bộ mạng lưới 400+ đại lý/xưởng dịch vụ xe điện toàn quốc, tăng tỷ lệ giữ chân khách hàng (retention rate), giảm quá tải hotline tổng đài cấp hãng, và cung cấp dashboard thời gian thực đo lường SLA & CSAT của từng đại lý."
    for r in p32.runs:
        style_run(r, size_pt=9.5)

    # TABLE 1: BẰNG CHỨNG BẰNG SỐ CHO LỰA CHỌN KÊNH
    t1 = doc.tables[1]
    t1.rows[1].cells[1].text = "$374  (9.500.000 VNĐ)"
    t1.rows[2].cells[1].text = "$3.804  (ACV: $4.488)"
    t1.rows[3].cells[1].text = "0,45 deal / ngày  (Khả thi số học)"
    t1.rows[4].cells[1].text = "$32.000  ($8.000 opp / 25% win)"
    t1.rows[5].cells[1].text = "8,4 lần  (Inside Sales BẤT KHẢ THI)"

    for r_idx in range(1, len(t1.rows)):
        for c_idx in [0, 1, 2]:
            cell = t1.rows[r_idx].cells[c_idx]
            for p in cell.paragraphs:
                for r in p.runs:
                    style_run(r, size_pt=9, bold=(c_idx==1))

    # PAIN MOMENT (P38)
    p38 = doc.paragraphs[38]
    p38.text = "Thứ 7, từ 08h30 đến 10h30 sáng (khung giờ cao điểm khách hẹn mang xe đi bảo dưỡng cuối tuần). Nhân viên CSKH đại lý vừa nghe điện thoại tư vấn vừa mở phần mềm DMS tra slot kỹ thuật viên, trong khi 2 khách khác đang nhắn tin dồn dập trên Zalo OA hỏi lịch bảo dưỡng xe VF8/VF9 nhưng không ai kịp trả lời khiến khách thoát chat sang đại lý đối thủ. Khách hàng đang dùng Zalo OA đại lý, điện thoại hotline và phần mềm quản trị DMS nội bộ."
    for r in p38.runs:
        style_run(r, size_pt=9.5, italic=True)

    # ĐIỂM NHÚNG (P42)
    p42 = doc.paragraphs[42]
    p42.text = "Zalo Official Account (OA) Webhook & Facebook Messenger Fanpage của Đại lý, tích hợp trực tiếp 2 chiều qua API với phần mềm DMS để kiểm tra và khóa slot kỹ thuật viên theo thời gian thực."
    for r in p42.runs:
        style_run(r, size_pt=9.5, bold=True)

    # TABLE 2: 90-DAY PLAN
    t2 = doc.tables[2]
    # Row 1: Kênh
    t2.rows[1].cells[1].text = "Founder-led Pilot trực tiếp"
    t2.rows[1].cells[2].text = "Partner-Led (VinFast Aftersales)"
    t2.rows[1].cells[3].text = "Mở rộng đại lý toàn quốc"
    # Row 2: Mục tiêu số khách
    t2.rows[2].cells[1].text = "2 đại lý 3S thí điểm"
    t2.rows[2].cells[2].text = "5 đại lý ủy quyền"
    t2.rows[2].cells[3].text = "15 đại lý mở rộng"
    # Row 3: Việc cụ thể
    t2.rows[3].cells[1].text = "• Deploy chatbot Zalo OA cho 2 đại lý quen thuộc.\n• Ngồi trực tiếp cùng CSKH 2 buổi/tuần bắt edge cases.\n• Đo lường containment rate trên 200 lượt booking đầu tiên."
    t2.rows[3].cells[2].text = "• Hoàn thiện Pilot Report gửi Giám đốc Aftersales VinFast.\n• Demo tại Hội nghị Giám đốc Dịch vụ Đại lý VinFast miền Bắc.\n• Ký thỏa thuận đối tác giải pháp chính thức."
    t2.rows[3].cells[3].text = "• Đóng gói bộ cài đặt chuẩn (plug & play) kết nối DMS.\n• Tổ chức webinar đào tạo trực tuyến cho 50+ Trưởng xưởng.\n• Thiết lập kênh hỗ trợ L2 và cam kết SLA 99.9%."
    # Row 4: KPI đo được
    t2.rows[4].cells[1].text = "200 booking, CR ≥ 75%, 0 lỗi trùng slot"
    t2.rows[4].cells[2].text = "5 đại lý active, 2.000 booking/tháng, GM ≥ 60%"
    t2.rows[4].cells[3].text = "15 đại lý, 6.000 booking/tháng, MRR > 140tr VNĐ"
    # Row 5: Ai chịu trách nhiệm
    t2.rows[5].cells[1].text = "Nguyễn Văn An (Founder/AI Lead)"
    t2.rows[5].cells[2].text = "Nguyễn Văn An + Advisor đối tác"
    t2.rows[5].cells[3].text = "Nguyễn Văn An + Kỹ sư Triển khai"

    for r_idx in range(1, len(t2.rows)):
        for c_idx in range(len(t2.columns)):
            cell = t2.rows[r_idx].cells[c_idx]
            for p in cell.paragraphs:
                for r in p.runs:
                    style_run(r, size_pt=8.5)

    # TABLE 3: EVIDENCE PACK
    t3 = doc.tables[3]
    # Row 1: Eval Results
    t3.rows[1].cells[1].text = "Chưa"
    t3.rows[1].cells[2].text = "Eval trên 50 ca smoke test đạt CR 80%; cần chạy eval chuẩn hóa trên 200 ca thực tế đại lý (đo intent, slot accuracy, handoff rate)."
    t3.rows[1].cells[3].text = "Nguyễn Văn An · 15/11/2026"
    # Row 2: Risk Checklist
    t3.rows[2].cells[1].text = "Rồi"
    t3.rows[2].cells[2].text = "Đã hoàn thiện tài liệu giải trình 3 rủi ro: Anthropic API không train data, cơ chế fallback CSKH khi confidence < 85%, data xuất SQL độc lập trên Supabase."
    t3.rows[2].cells[3].text = "Nguyễn Văn An · 08/10/2026"
    # Row 3: Pilot Report
    t3.rows[3].cells[1].text = "Chưa"
    t3.rows[3].cells[2].text = "Báo cáo kết quả thí điểm 4 tuần tại 2 đại lý: 200 booking, CR 80%, tiết kiệm 20h CSKH/tuần, tăng 15% booking dịch vụ ngoài giờ."
    t3.rows[3].cells[3].text = "Nguyễn Văn An · 30/11/2026"

    for r_idx in range(1, len(t3.rows)):
        for c_idx in range(len(t3.columns)):
            cell = t3.rows[r_idx].cells[c_idx]
            for p in cell.paragraphs:
                for r in p.runs:
                    style_run(r, size_pt=8.5, bold=(c_idx in [0, 1]))

    # BÀI TEST NGƯỜI LẠ (P50, P51, P52, P53)
    p50 = doc.paragraphs[50]
    p50.text = "☑  Bạn bán gì, cho ai, tính tiền theo đơn vị nào?  → Bán AI Agent đặt hẹn bảo dưỡng cho đại lý xe VinFast; tính 1,5tr nền + 20k/booking confirmed."
    for r in p50.runs:
        style_run(r, size_pt=9.5, color_rgb=(0, 102, 0))

    p51 = doc.paragraphs[51]
    p51.text = "☑  Có lãi trên mỗi đơn vị không — con số nào chứng minh?  → Lãi tốt: Cost biến phí 5.334 VNĐ ($0,210), giá bán 35.000 VNĐ ($1,378), Gross Margin 84,8%."
    for r in p51.runs:
        style_run(r, size_pt=9.5, color_rgb=(0, 102, 0))

    p52 = doc.paragraphs[52]
    p52.text = "☑  Tiếp cận khách qua đâu — và vì sao là kênh đó?  → Partner-Led qua VinFast Vietnam Aftersales Division vì Inside Sales CAC ($32k) lệch 8,4× ngân sách."
    for r in p52.runs:
        style_run(r, size_pt=9.5, color_rgb=(0, 102, 0))

    p53 = doc.paragraphs[53]
    p53.text = "Số câu người đọc phải hỏi lại: 1 câu (người đọc hỏi rõ về cách kết nối API với phần mềm DMS của VinFast — mục tiêu ≤ 3 câu: ĐẠT)."
    for r in p53.runs:
        style_run(r, size_pt=9.5, bold=True, color_rgb=(0, 51, 102))

    # Format header/footer or margins if needed
    for section in doc.sections:
        section.top_margin = Inches(0.6)
        section.bottom_margin = Inches(0.6)
        section.left_margin = Inches(0.65)
        section.right_margin = Inches(0.65)

    output_student = 'NguyenVanAn_Day22_onepager.docx'
    doc.save(output_student)
    print(f'Successfully saved {output_student}')
    
    doc.save('Day22-AI-Product-GTM-One-Pager-Template.docx')
    print('Successfully updated Day22-AI-Product-GTM-One-Pager-Template.docx')

if __name__ == '__main__':
    build_docx()
