import openpyxl, sys
sys.stdout.reconfigure(encoding='utf-8')

def build_excel():
    template_path = 'Day22-AI-Product-GTM-Monetization-Model.xlsx'
    wb = openpyxl.load_workbook(template_path)
    
    # -------------------------------------------------------------
    # TAB 1: 1_Cost_Job
    # -------------------------------------------------------------
    ws1 = wb['1_Cost_Job']
    ws1['B5'] = "1 lịch bảo dưỡng xe VinFast được xác nhận thành công (booking status = CONFIRMED, có SMS xác nhận cho khách và ghi nhận vào lịch kỹ thuật viên đại lý)"
    ws1['B6'] = "A" # Biến thể A: Bán SaaS cho đại lý, đại lý tự chịu escalation
    ws1['B9'] = 500.0 # Số job thử / tháng
    ws1['B10'] = 0.80 # Containment rate 80% (smoke test 50 ca)
    
    # LLM Claude Haiku 4.5
    ws1['B15'] = 1.0 # Input ($ / 1M token)
    ws1['B16'] = 5.0 # Output ($ / 1M token)
    ws1['B17'] = 1.25 # Cache WRITE
    ws1['B18'] = 0.10 # Cache READ
    ws1['B19'] = 5.0 # Số lượt (turns) / job
    ws1['B20'] = 2800.0 # Token CACHE / lượt (system prompt + VinFast service catalog RAG)
    ws1['B21'] = 700.0 # Token FRESH / lượt (tin nhắn khách + xe)
    ws1['B22'] = 250.0 # Token output / lượt
    ws1['B30'] = 0.0 # Không dùng Batch API
    
    # Speech
    ws1['B34'] = 0.0
    ws1['B35'] = 0.0
    ws1['B36'] = 0.0
    ws1['B37'] = 0.0
    
    # Infra
    # Supabase $25 + Railway $5 + SMS (400*600đ=240k=9.45$) = $39.45 to $41.81/tháng.
    # $41.80 / 500 job thử = 0.0836 $/job thử -> chia 400 completed = 0.1045 $/job completed!
    ws1['B41'] = 0.0836
    ws1['B42'] = 0.0
    
    # Retry
    ws1['B46'] = 0.07 # 7% retry
    
    # HITL
    ws1['B50'] = 9.0 # $9.0/giờ (CSKH / QA tech fully loaded tại VN ~228.000đ/h)
    ws1['B51'] = 0.05 # 5% ca QA nội bộ
    # 9.2 phút = 3 phút QA review ca mẫu + thời gian phân bổ bảo trì/drift calibration
    ws1['B52'] = 9.2 
    ws1['B53'] = 6.0 # Escalation time (Biến thể A nên công thức B55 = 0)
    
    # Overhead
    ws1['B59'] = 400.0 # R&D ($200) + Sales founder ($200) = $400/tháng
    ws1['B68'] = 25400.0 # Tỷ giá 25.400đ/USD (Vietcombank 08/10/2026)
    
    # -------------------------------------------------------------
    # TAB 2: 2_Pricing
    # -------------------------------------------------------------
    ws2 = wb['2_Pricing']
    ws2['B6'] = 3.0 # Hệ số an toàn tối thiểu (3x)
    ws2['B10'] = 2500.0 # Giá trị khách tiết kiệm/nhận được: 63,5 triệu đ (~$2.500) từ thu thêm 125 booking ngoài giờ + tiết kiệm ca trực
    ws2['B11'] = 400.0 # Số job hoàn thành / tháng của 1 khách
    ws2['B14'] = 800.0 # Lương CSKH trực ca: 20 triệu đ (~$800)
    ws2['B19'] = 1.378 # Giá bán đề xuất: $1,378/job (= 35.000₫/job)
    ws2['B32'] = 0.60 # Gross Margin mục tiêu (60%)
    
    # -------------------------------------------------------------
    # TAB 3: 3_Value_Metric
    # -------------------------------------------------------------
    ws3 = wb['3_Value_Metric']
    # Attribution
    ws3['B5'] = 2.0 # Log đầy đủ từng step, status CONFIRMED
    ws3['B6'] = 2.0 # Eval dataset 50 ca ground truth
    ws3['B7'] = 2.0 # Khách đại lý đồng ý: chỉ tính tiền booking CONFIRMED
    ws3['B8'] = 1.0 # Flag created_by='ai_agent', khách có thể gọi lại kiểm tra
    ws3['B9'] = 2.0 # Định nghĩa chặt: CONFIRMED = tính tiền; escalate/hủy = 0đ
    
    # Autonomy
    ws3['B13'] = 2.0 # AI hoàn thành end-to-end trong happy path
    ws3['B14'] = 2.0 # Chạy 24/7 ngoài giờ không cần nhân viên trực
    ws3['B15'] = 2.0 # Tự động handoff khi xe tai nạn / ca phức tạp
    ws3['B16'] = 2.0 # Tỷ lệ can thiệp 20% (containment rate đạt 80%)
    ws3['B17'] = 1.0 # QA kiểm tra mẫu 5% ca
    
    # Benchmark
    ws3['A26'] = "Intercom Fin"
    ws3['B26'] = "Outcome (Resolution)"
    ws3['C26'] = "$0,99 / resolution"
    ws3['D26'] = "https://fin.ai/pricing/"
    
    ws3['A27'] = "Salesforce Agentforce"
    ws3['B27'] = "Hybrid (Platform fee + per Action)"
    ws3['C27'] = "$5/user/tháng + $0,10/action"
    ws3['D27'] = "https://salesforce.com/agentforce/pricing/"
    
    # Quyết định cuối
    ws3['B30'] = "Hybrid"
    ws3['B31'] = "Thị trường đại lý ô tô tại Việt Nam chưa quen trả 100% outcome thuần do ngại rủi ro biến động chi phí. Mô hình Hybrid (phí nền 1.500.000₫/tháng + 20.000₫/booking confirmed) giúp đại lý dễ lập kế hoạch ngân sách hàng tháng, đồng thời bảo đảm dòng tiền bù đắp chi phí cố định (server, DB, support) cho startup ngay từ những tháng đầu."
    ws3['B32'] = "Tôi chọn mô hình Hybrid gồm phí nền cố định 1.500.000₫/tháng/đại lý kết hợp 20.000₫/lịch bảo dưỡng xác nhận thành công (booking status = CONFIRMED)."
    ws3['B33'] = "Điểm Attribution đạt 9/10 (log minh bạch mã booking trên DMS và SMS brandname gửi thành công) và Autonomy đạt 9/10 (AI tự động 80% quy trình 24/7 theo smoke test 50 ca)."
    ws3['B34'] = "Mô hình này lỗ khi tỷ lệ containment tụt dưới 30,5% kết hợp số lượng đại lý dưới 3, khiến doanh thu không bù nổi chi phí nhân sự QA và hạ tầng cố định."
    
    # -------------------------------------------------------------
    # TAB 4: 4_Channel_Fit
    # -------------------------------------------------------------
    ws4 = wb['4_Channel_Fit']
    ws4['B5'] = 374.0 # ARPU: 9.500.000₫ = $374/tháng (1.5M nền + 400*20k)
    ws4['B7'] = "SMB" # Đại lý 3S/1S VinFast
    ws4['B13'] = 500000.0 # Quota AE / năm
    ws4['B14'] = 250.0 # Ngày làm việc / năm
    ws4['B20'] = 8000.0 # Cost per opportunity
    ws4['B21'] = 0.25 # Win rate 25%
    
    # Chấm điểm 3 kênh (B: PLG, C: Sales-Led, D: Partner-Led)
    # 1. CAC nuôi nổi
    ws4['B28'] = 4.0; ws4['C28'] = 1.0; ws4['D28'] = 5.0
    # 2. Khách mua theo cách này
    ws4['B29'] = 2.0; ws4['C29'] = 3.0; ws4['D29'] = 5.0
    # 3. Đội có năng lực chạy ngay
    ws4['B30'] = 2.0; ws4['C30'] = 2.0; ws4['D30'] = 4.0
    # 4. Tiếp cận điểm nhúng / partner 30 ngày
    ws4['B31'] = 2.0; ws4['C31'] = 2.0; ws4['D31'] = 4.0
    # 5. Đưa đến đúng Pain Moment
    ws4['B32'] = 3.0; ws4['C32'] = 3.0; ws4['D32'] = 5.0
    # 6. Đo hiệu quả trong 90 ngày
    ws4['B33'] = 3.0; ws4['C33'] = 2.0; ws4['D33'] = 5.0
    
    ws4['B38'] = "Partner-Led"
    ws4['B39'] = "VinFast Vietnam (Bộ phận Dịch vụ Hậu mãi & Mạng lưới Đại lý - Aftersales & Dealer Network)"
    ws4['B40'] = "Chưa"
    ws4['B41'] = "Giúp VinFast chuẩn hóa quy trình tiếp nhận dịch vụ sau bán hàng của toàn bộ mạng lưới 400+ đại lý/xưởng dịch vụ, tăng tỷ lệ giữ chân khách hàng xe điện, giảm quá tải hotline tổng đài, và cung cấp dashboard thời gian thực đo lường chỉ số CSAT & tỷ lệ chuyển đổi dịch vụ."
    ws4['B42'] = "Nếu kênh Partner-Led bị chậm do thủ tục nội bộ VinFast, lối thoát dự phòng là chuyển sang Founder-Led Direct Sales tiếp cận trực tiếp 3–5 chủ đại lý 3S tư nhân lớn tại Hà Nội/TP.HCM (mô hình hybrid sales tập trung vào ROI ngắn hạn) trước khi ký phân phối toàn hệ thống."
    
    # -------------------------------------------------------------
    # TAB 5: 5_90Day_Plan
    # -------------------------------------------------------------
    ws5 = wb['5_90Day_Plan']
    # Pain moment
    ws5['B5'] = "Thứ 7, từ 08h30 đến 10h30 sáng (khung giờ cao điểm khách hẹn xe cuối tuần)"
    ws5['B6'] = "Nhân viên CSKH vừa nghe điện thoại tư vấn vừa mở phần mềm DMS tra slot kỹ thuật viên, trong khi 2 khách khác nhắn dồn dập trên Zalo OA hỏi lịch trống cuối tuần không được phản hồi kịp thời và thoát ra."
    ws5['B7'] = "Zalo OA đại lý, Hotline điện thoại và phần mềm DMS"
    ws5['B8'] = "Zalo Official Account (OA) Webhook & Facebook Messenger Fanpage của Đại lý, tích hợp trực tiếp 2 chiều qua API với DMS để kiểm tra và khóa slot kỹ thuật viên theo thời gian thực."
    
    # 90-Day Plan (B: Tháng 1, C: Tháng 2-3, D: Tháng 4+)
    ws5['B12'] = "Founder-led Pilot trực tiếp"
    ws5['C12'] = "Partner-Led (VinFast Aftersales)"
    ws5['D12'] = "Mở rộng đại lý toàn quốc"
    
    ws5['B13'] = "2 đại lý 3S thí điểm"
    ws5['C13'] = "5 đại lý ủy quyền"
    ws5['D13'] = "15 đại lý mở rộng"
    
    ws5['B14'] = "Deploy chatbot Zalo OA cho 2 đại lý quen thuộc, theo dõi log từng booking"
    ws5['C14'] = "Hoàn thiện Pilot Report có số liệu thực tế gửi Giám đốc Aftersales VinFast"
    ws5['D14'] = "Đóng gói bộ cài đặt chuẩn (plug & play) kết nối DMS toàn bộ mạng lưới"
    
    ws5['B15'] = "Ngồi trực tiếp cùng nhân viên CSKH 2 buổi/tuần để ghi nhận edge case và bổ sung few-shot prompt"
    ws5['C15'] = "Thuyết trình demo tại Hội nghị Giám đốc Dịch vụ Đại lý VinFast miền Bắc"
    ws5['D15'] = "Tổ chức webinar đào tạo trực tuyến cho 50+ Trưởng xưởng dịch vụ"
    
    ws5['B16'] = "Đo lường containment rate thực tế trên 200 lượt booking đầu tiên và tối ưu cache"
    ws5['C16'] = "Ký thỏa thuận đối tác giải pháp chính thức với bộ phận Aftersales VinFast"
    ws5['D16'] = "Thiết lập kênh hỗ trợ kỹ thuật cấp 2 (L2 support) và cam kết SLA 99.9%"
    
    ws5['B17'] = "200 booking, CR ≥ 75%, 0 lỗi trùng lịch hẹn"
    ws5['C17'] = "5 đại lý active, 2.000 booking/tháng, GM ≥ 60%"
    ws5['D17'] = "15 đại lý, 6.000 booking/tháng, MRR > 140 triệu VNĐ"
    
    ws5['B18'] = "Nguyễn Văn An (Founder / AI Lead)"
    ws5['C18'] = "Nguyễn Văn An + Advisor quan hệ đối tác"
    ws5['D18'] = "Nguyễn Văn An + Kỹ sư Triển khai (Deploy Engineer)"
    
    # Evidence Pack
    ws5['B23'] = "Chưa"
    ws5['C23'] = "Eval trên 50 ca smoke test đạt CR 80%; cần chạy eval chuẩn hóa trên 200 ca thực tế đại lý (đo intent, slot accuracy, handoff rate)."
    ws5['D23'] = "Nguyễn Văn An · 15/11/2026"
    
    ws5['B24'] = "Rồi"
    ws5['C24'] = "Đã hoàn thiện tài liệu giải trình 3 rủi ro: Anthropic API không train data, cơ chế fallback CSKH khi confidence < 85%, data xuất SQL độc lập trên Supabase."
    ws5['D24'] = "Nguyễn Văn An · 08/10/2026"
    
    ws5['B25'] = "Chưa"
    ws5['C25'] = "Báo cáo kết quả thí điểm 4 tuần tại 2 đại lý: 200 booking, CR 80%, tiết kiệm 20h CSKH/tuần, tăng 15% booking dịch vụ ngoài giờ."
    ws5['D25'] = "Nguyễn Văn An · 30/11/2026"
    
    # Bài test người lạ
    ws5['B29'] = "Được"
    ws5['B30'] = "Được"
    ws5['B31'] = "Được"
    ws5['B32'] = 1
    
    # -------------------------------------------------------------
    # TAB 6: 6_Benchmarks
    # -------------------------------------------------------------
    ws6 = wb['6_Benchmarks']
    ws6['B3'] = "08/10/2026"
    
    # Lưu ra cả 2 file: template cập nhật & file nộp theo tên học viên
    output_student = 'NguyenVanAn_Day22_model.xlsx'
    wb.save(output_student)
    print(f'Successfully saved {output_student}')
    
    wb.save(template_path)
    print(f'Successfully updated {template_path}')

if __name__ == '__main__':
    build_excel()
