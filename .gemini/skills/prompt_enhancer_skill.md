# 🧠 Auto Prompt Engineer Skill — v2.0 Pro Edition

> **Version:** 2.0 Pro · **Updated:** 2026-04-19 · **Category:** Prompt Engineering  
> **Changelog v2.0:** Domain auto-detect with 8 categories, 6 PE techniques (Persona Stacking, CoT, Negative Prompting, Few-Shot, Quality Gate, Iterative Refinement), 5 domain-specific templates, processing pipeline with context mining, adaptive behavior, cross-skill integration.

---

## 1. Mục tiêu (Objective)
Biến BẤT KỲ câu lệnh thô nào (dù ngắn 3 từ hay dài lộn xộn) thành một **prompt cấp chuyên gia** — chi tiết, có cấu trúc, tuân thủ các kỹ thuật prompt engineering tiên tiến nhất — sẵn sàng nạp cho bất kỳ AI model nào (Claude, Gemini, ChatGPT, Copilot...) và nhận kết quả chất lượng cao ngay từ lần chạy đầu tiên.

**Cross-skill Integration:**
- Prompt cho coding task → tự kèm **Architecture Planner** best practices
- Prompt cho hardware task → tự inject cảnh báo GPIO conflicts từ **Debug Detective** memory
- Prompt cho luận văn → tự format theo **Smart Docs Generator** TDTU template
- Prompt yêu cầu code → gợi ý dùng **Snippet Factory** sau khi nhận kết quả

---

## 2. Trigger — Khi nào kích hoạt Skill này

| Trigger Pattern | Ví dụ người dùng nói |
|---|---|
| Yêu cầu tạo/viết prompt | *"tạo prompt cho tao..."*, *"viết prompt giúp..."* |
| Yêu cầu nâng cấp prompt | *"nâng cấp prompt này..."*, *"cải thiện prompt..."* |
| Đưa ý tưởng thô muốn chi tiết hóa | *"viết code app quản lý chi tiêu"* rồi nói *"tạo prompt cho cái này"* |
| Lười viết chi tiết | *"lười viết quá, prompt dùm..."*, *"expand cái này ra..."* |
| Dùng từ khóa ngắn | *"prompt: ..."*, *"enhance: ..."*, *"PE: ..."* |

---

## 3. Bảng phân loại Domain tự động (Auto Domain Detection)

Khi nhận câu lệnh thô, hãy tự động phân loại nó vào đúng domain để áp dụng **template chuyên biệt**:

| Domain | Keywords nhận diện | Template ưu tiên |
|---|---|---|
| 🖥️ **Coding / Dev** | code, script, app, api, web, backend, frontend, database | `CODING_TEMPLATE` |
| 🎨 **Design / UI-UX** | design, UI, giao diện, mockup, logo, banner, figma | `DESIGN_TEMPLATE` |
| ✍️ **Writing / Content** | viết bài, blog, email, thư, essay, báo cáo, luận văn | `WRITING_TEMPLATE` |
| 📊 **Data / Analysis** | phân tích, data, biểu đồ, thống kê, excel, dashboard | `DATA_TEMPLATE` |
| 🤖 **AI / ML** | model, train, dataset, fine-tune, inference, neural | `AI_ML_TEMPLATE` |
| 🔧 **Hardware / IoT** | ESP32, Arduino, sensor, motor, PCB, robot, firmware | `HARDWARE_TEMPLATE` |
| 📚 **Learning / Research** | giải thích, so sánh, tóm tắt, nghiên cứu, học | `LEARNING_TEMPLATE` |
| 🧩 **General / Khác** | Không rõ domain | `UNIVERSAL_TEMPLATE` |

---

## 4. Kỹ thuật Prompt Engineering nâng cao được tích hợp

Skill này KHÔNG chỉ "viết dài hơn". Nó áp dụng có chọn lọc các kỹ thuật PE đã được chứng minh hiệu quả:

### 4.1 — Persona Stacking (Xếp chồng vai trò)
Khi task phức tạp đòi hỏi nhiều chuyên môn, gán cho AI **nhiều vai trò bổ trợ** thay vì chỉ 1.
```
Bạn đồng thời là:
- Senior React Developer (code architecture)
- UX Designer (user flow & accessibility)  
- Performance Engineer (optimization & lazy loading)
```

### 4.2 — Chain-of-Thought (CoT) Injection
Yêu cầu AI "suy nghĩ từng bước" trước khi đưa ra kết quả cuối:
```
Trước khi code, hãy:
1. Phân tích yêu cầu → liệt kê các component cần thiết
2. Thiết kế data flow → state management approach  
3. Sau đó mới bắt đầu implement
```

### 4.3 — Negative Prompting (Nói rõ KHÔNG được làm gì)
Giảm thiểu kết quả rác bằng cách chỉ rõ những gì AI phải tránh:
```
❌ KHÔNG được:
- Sử dụng any type trong TypeScript
- Hard-code giá trị magic number
- Bỏ qua error handling
- Trả về code thiếu comment
```

### 4.4 — Few-Shot Examples (Cho ví dụ mẫu)
Khi output cần format cụ thể, đính kèm 1-2 ví dụ mẫu input → output.

### 4.5 — Quality Gate (Tiêu chí tự đánh giá)
Yêu cầu AI tự kiểm tra output trước khi trả về:
```
Trước khi trả kết quả, hãy tự kiểm tra:
□ Code có chạy được không? (no syntax errors)
□ Có xử lý edge cases chưa?
□ Có tuân thủ tất cả constraints không?
□ Output format có đúng yêu cầu không?
```

### 4.6 — Iterative Refinement Hooks (Móc cải tiến)
Thêm câu cuối prompt cho phép user dễ dàng tinh chỉnh kết quả:
```
Sau khi hoàn thành, hãy hỏi tôi:
"Bạn muốn điều chỉnh phần nào? (1) Thêm tính năng (2) Đổi phong cách (3) Tối ưu performance"
```

---

## 5. Templates chuyên biệt theo Domain

### 5.1 — `CODING_TEMPLATE`
```markdown
## 🖥️ PROMPT — [Tên Task]

**🎭 Vai trò:**
Bạn là [Senior/Staff ...]  Developer chuyên về [tech stack]. Bạn có kinh nghiệm sâu về [specific domain] và luôn viết code production-ready.

**📋 Bối cảnh:**
[Mô tả dự án, tech stack hiện tại, vấn đề đang gặp, mục tiêu dự án]

**🎯 Nhiệm vụ:**
[Mô tả chi tiết task cần làm — càng cụ thể càng tốt]

**⚙️ Yêu cầu kỹ thuật:**
1. Ngôn ngữ / Framework: [...]
2. Design patterns: [...]
3. Error handling: [mô tả cách xử lý lỗi]
4. Security: [yêu cầu bảo mật nếu có]
5. Performance: [yêu cầu hiệu năng nếu có]

**🚫 Constraints (Ràng buộc):**
- KHÔNG [...]
- PHẢI [...]
- TRÁNH [...]

**📤 Định dạng đầu ra:**
- [ ] File structure rõ ràng
- [ ] Code có comment giải thích logic phức tạp
- [ ] Kèm hướng dẫn chạy (README ngắn)
- [ ] [Thêm yêu cầu format khác...]

**🔄 Sau khi hoàn thành:**
Hãy tự review code và liệt kê 3 điểm có thể cải thiện thêm.
```

### 5.2 — `DESIGN_TEMPLATE`
```markdown
## 🎨 PROMPT — [Tên Design Task]

**🎭 Vai trò:**
Bạn là Senior UI/UX Designer kiêm Frontend Developer với thẩm mỹ cao cấp, chuyên thiết kế giao diện modern, premium.

**📋 Bối cảnh:**
[Loại sản phẩm, đối tượng người dùng, brand identity, mood/tone mong muốn]

**🎯 Nhiệm vụ:**
[Mô tả chi tiết screen/component cần design]

**🎨 Design Direction:**
- Color Palette: [dark mode / light mode / specific colors]
- Typography: [font family, hierarchy]
- Style: [glassmorphism / neomorphism / flat / material / ...]
- Animations: [micro-interactions, transitions, hover effects]
- Inspiration: [reference websites/apps nếu có]

**📐 Specifications:**
- Responsive: [mobile-first / desktop-first / breakpoints cụ thể]
- Accessibility: [WCAG level, contrast ratio]
- Component library: [nếu dùng existing library]

**📤 Định dạng đầu ra:**
[HTML+CSS / Figma specs / React components / ...]
```

### 5.3 — `WRITING_TEMPLATE`
```markdown
## ✍️ PROMPT — [Tên bài viết/văn bản]

**🎭 Vai trò:**
Bạn là [chuyên gia viết content / copywriter / academic writer / ...] với phong cách [tone: chuyên nghiệp / thân thiện / học thuật / sáng tạo].

**📋 Bối cảnh:**
[Viết cho ai? Đăng ở đâu? Mục đích gì? Độ dài mong muốn?]

**🎯 Nhiệm vụ:**
[Nội dung chính cần viết]

**📝 Yêu cầu nội dung:**
- Tone/Voice: [formal / casual / persuasive / informative]
- Cấu trúc: [có heading / bullet points / numbered list / paragraphs]
- Độ dài: [~ số từ hoặc số trang]
- SEO keywords (nếu cần): [...]
- CTA (Call to Action) nếu cần: [...]

**🚫 Tránh:**
- [Không dùng từ ngữ quá hàn lâm / quá casual / ...]
- [Không copy paste thông tin chưa xác minh]

**📤 Định dạng đầu ra:**
[Markdown / Google Docs format / HTML / Plain text]
```

### 5.4 — `HARDWARE_TEMPLATE`
```markdown
## 🔧 PROMPT — [Tên project phần cứng]

**🎭 Vai trò:**
Bạn là Embedded Systems Engineer chuyên về [ESP32 / Arduino / STM32 / ...], có kinh nghiệm thực tế với [sensors / motors / communication protocols].

**📋 Bối cảnh:**
[Mô tả dự án phần cứng, board đang dùng, mục đích, hệ thống tổng thể]

**🎯 Nhiệm vụ:**
[Viết firmware / thiết kế mạch / debug vấn đề cụ thể]

**⚙️ Hardware Specs:**
- MCU: [model cụ thể, ví dụ ESP32-S3-WROOM-1]
- Peripherals: [sensors, actuators, displays...]
- Communication: [UART, I2C, SPI, WiFi, BLE...]
- Power: [nguồn cấp, pin, voltage levels]

**💻 Software Requirements:**
- Framework: [Arduino / ESP-IDF / PlatformIO / MicroPython]
- Libraries: [thư viện cần dùng]
- Pin mapping: [bảng GPIO nếu cần]

**⚠️ Lưu ý phần cứng:**
- [GPIO conflicts cần tránh]
- [Giới hạn dòng/áp]
- [Thermal considerations]

**📤 Định dạng đầu ra:**
[Code firmware hoàn chỉnh / Sơ đồ mạch / BOM list / ...]
```

### 5.5 — `UNIVERSAL_TEMPLATE` (Fallback cho mọi domain)
```markdown
## 🧩 PROMPT — [Tên Task]

**🎭 Vai trò:**
Bạn là chuyên gia hàng đầu trong lĩnh vực [auto-detect]. 

**📋 Bối cảnh:**
[Context đầy đủ]

**🎯 Nhiệm vụ:**  
[Task description chi tiết]

**📌 Yêu cầu cụ thể:**
1. [Requirement 1]
2. [Requirement 2]
3. [...]

**🚫 Ràng buộc:**
- [Constraint 1]
- [Constraint 2]

**💡 Gợi ý approach (Chain-of-Thought):**
Hãy thực hiện theo các bước:
1. Phân tích yêu cầu
2. Lên kế hoạch giải quyết
3. Triển khai
4. Tự review kết quả

**📤 Định dạng đầu ra:**
[Describe expected output format]

**🔄 Refinement:**
Sau khi hoàn thành, đề xuất 2-3 hướng cải thiện hoặc mở rộng.
```

---

## 6. Workflow xử lý (Processing Pipeline)

Khi nhận Raw Prompt từ người dùng, thực hiện pipeline sau:

```
┌─────────────────────────────────────────────────────┐
│  RAW INPUT: "viết app quản lý chi tiêu bằng react"  │
└──────────────────────┬──────────────────────────────┘
                       ▼
         ┌─────────────────────────┐
         │  STEP 1: INTENT PARSING │
         │  → Core intent: gì?     │
         │  → Domain: nào?         │
         │  → Complexity: cao/thấp │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │  STEP 2: CONTEXT MINING │
         │  → Đọc workspace hiện   │
         │    tại (nếu có)         │
         │  → Kiểm tra tech stack  │
         │    user hay dùng        │
         │  → Check conversation   │ 
         │    history              │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │ STEP 3: GAP FILLING     │
         │ → Best practices        │
         │ → Security patterns     │
         │ → Error handling        │
         │ → Performance tips      │
         │ → Architecture patterns │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │ STEP 4: TEMPLATE SELECT │
         │ → Chọn domain template  │
         │ → Áp dụng PE techniques │
         │ → Inject CoT nếu cần   │
         │ → Add negative prompts  │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │ STEP 5: QUALITY CHECK   │
         │ → Đủ context chưa?      │
         │ → Có mâu thuẫn không?   │
         │ → Tone phù hợp chưa?   │
         │ → Quá dài/quá ngắn?    │
         └────────────┬────────────┘
                      ▼
         ┌─────────────────────────┐
         │ STEP 6: OUTPUT          │
         │ → Bọc trong code block  │
         │ → Kèm metadata ngắn    │
         │ → Suggest next steps    │
         └─────────────────────────┘
```

---

## 7. Output Format — Cách trình bày kết quả

Khi trả kết quả cho người dùng, hãy tuân thủ format sau:

### Header (Trước code block)
```
🚀 **Prompt đã được nâng cấp!**
- 📂 Domain: [Coding / Design / Writing / ...]
- 🎯 Độ phức tạp: [Đơn giản / Trung bình / Phức tạp]
- 🛠️ Kỹ thuật PE áp dụng: [Persona Stacking, CoT, Negative Prompting, ...]
- 📋 Tối ưu cho model: [General / Claude / Gemini / ChatGPT]
```

### Body (Code block chứa prompt)
Bọc toàn bộ Enhanced Prompt trong code block có language tag `text` hoặc `markdown` để user dễ copy:
````
```text
[ENHANCED PROMPT Ở ĐÂY]
```
````

### Footer (Sau code block)
```
💡 **Gợi ý tinh chỉnh thêm:**
1. [Suggestion 1 - ví dụ: "Thêm requirement về testing"]
2. [Suggestion 2 - ví dụ: "Chỉ định database cụ thể"]
3. [Suggestion 3 - ví dụ: "Thêm constraint về deployment"]

📌 Nói "chỉnh [số]" để tôi thêm gợi ý đó vào prompt.
```

---

## 8. Ví dụ minh họa đầy đủ

### Ví dụ 1 — Coding Domain
**Raw Input:** `"viết app quản lý chi tiêu"`

**Enhanced Output:**

🚀 **Prompt đã được nâng cấp!**
- 📂 Domain: Coding
- 🎯 Độ phức tạp: Trung bình
- 🛠️ PE techniques: Persona Stacking, CoT, Negative Prompting, Quality Gate

```text
## 🖥️ PROMPT — App Quản lý Chi tiêu Cá nhân

**🎭 Vai trò:**  
Bạn đồng thời là:
- Senior Fullstack Developer chuyên React + Node.js, có kinh nghiệm xây dựng SaaS products
- UX Designer hiểu về personal finance UX patterns
- Database Architect quen thiết kế schema cho financial data

**📋 Bối cảnh:**  
Tôi cần xây dựng một ứng dụng web quản lý chi tiêu cá nhân. App cần đơn giản để dùng hàng ngày nhưng vẫn cung cấp insights hữu ích về thói quen chi tiêu. Đối tượng người dùng là sinh viên và người đi làm trẻ (20-30 tuổi) tại Việt Nam.

**🎯 Nhiệm vụ:**  
Thiết kế và code một ứng dụng quản lý chi tiêu cá nhân hoàn chỉnh với các chức năng:
- Thêm/sửa/xóa giao dịch thu-chi
- Phân loại chi tiêu theo danh mục (ăn uống, di chuyển, giải trí...)
- Dashboard thống kê theo ngày/tuần/tháng với biểu đồ trực quan
- Đặt ngân sách hàng tháng và cảnh báo khi vượt ngưỡng

**⚙️ Yêu cầu kỹ thuật:**
1. Frontend: React 18+ với Vite, sử dụng TypeScript
2. State management: Zustand hoặc React Context
3. UI: Thiết kế dark mode mặc định, responsive mobile-first
4. Storage: localStorage cho MVP, cấu trúc sẵn để migrate sang backend sau
5. Charts: Recharts hoặc Chart.js cho biểu đồ thống kê
6. Số liệu hiển thị theo VNĐ, format theo chuẩn Việt Nam (1.000.000đ)

**🚫 Ràng buộc:**
- KHÔNG sử dụng CSS framework (viết Vanilla CSS hoặc CSS Modules)
- KHÔNG hard-code dữ liệu mẫu — phải có flow onboarding cho user mới
- KHÔNG bỏ qua validation input (số âm, ký tự đặc biệt, format ngày)
- TRÁNH over-engineering — giữ code đơn giản, dễ maintain

**💡 Approach (Chain-of-Thought):**
Thực hiện theo thứ tự:
1. Thiết kế data models và TypeScript interfaces
2. Xây dựng utility functions (format currency, date helpers, category management)
3. Implement core CRUD operations
4. Xây dựng UI components (TransactionForm, TransactionList, Dashboard, Charts)
5. Kết nối state management
6. Polish UI/UX, thêm animations và responsive design

**📤 Định dạng đầu ra:**
- File structure tree đầu tiên
- Từng file code hoàn chỉnh, có comment giải thích
- README.md với hướng dẫn cài đặt và chạy

**✅ Self-Review Checklist:**
Trước khi trả kết quả, tự kiểm tra:
□ App có chạy được ngay bằng `npm run dev` không?
□ Responsive trên mobile không?
□ Dark mode có nhất quán không?
□ Có xử lý edge cases (empty state, số 0, negative numbers)?
□ UX có smooth không (transitions, loading states)?
```

💡 **Gợi ý tinh chỉnh thêm:**
1. Thêm tính năng export CSV/PDF báo cáo tháng
2. Thêm recurring transactions (chi tiêu định kỳ)
3. Thêm multi-currency support

📌 Nói **"chỉnh 1"**, **"chỉnh 2"**, hoặc **"chỉnh 3"** để tôi cập nhật thêm vào prompt.

---

### Ví dụ 2 — Writing Domain  
**Raw Input:** `"viết mail xin thực tập"`

**Enhanced Output:**

🚀 **Prompt đã được nâng cấp!**
- 📂 Domain: Writing  
- 🎯 Độ phức tạp: Đơn giản
- 🛠️ PE techniques: Persona, Few-Shot, Negative Prompting

```text
## ✍️ PROMPT — Email Xin Thực tập Chuyên nghiệp

**🎭 Vai trò:**  
Bạn là Career Coach chuyên giúp sinh viên Việt Nam viết email ứng tuyển chuyên nghiệp, có kinh nghiệm coaching cho các công ty tech hàng đầu.

**📋 Bối cảnh:**  
Tôi là sinh viên năm cuối ngành [ngành học] tại [tên trường]. Tôi muốn gửi email xin vị trí thực tập tại [tên công ty/lĩnh vực]. Thông tin cá nhân: [GPA, skills chính, project nổi bật].

**🎯 Nhiệm vụ:**
Viết một email xin thực tập bằng tiếng Việt (hoặc tiếng Anh — tôi sẽ chỉ định), nội dung chuyên nghiệp, gây ấn tượng nhưng không sáo rỗng.

**📝 Yêu cầu:**
- Tone: chuyên nghiệp nhưng chân thành, thể hiện được sự nhiệt huyết
- Độ dài: 200-300 từ (không quá dài, HR bận)
- Cấu trúc: Subject line hấp dẫn → Giới thiệu ngắn → Lý do chọn công ty (cụ thể, không generic) → Điểm mạnh bản thân → CTA rõ ràng
- Phải có placeholder [BRACKETS] cho thông tin cá nhân để tôi điền vào

**🚫 KHÔNG được:**
- Viết kiểu "Em là sinh viên chăm chỉ, cần cù" — quá generic
- Dùng ngôn ngữ quá trang trọng kiểu hành chính
- Copy paste những mẫu email cũ kỹ trên mạng

**📤 Đầu ra:**
Xuất 2 phiên bản: 1 bản tiếng Việt, 1 bản tiếng Anh. Mỗi bản bao gồm Subject line.
```

---

## 9. Quy tắc vàng khi sinh Prompt

1. **CỤ THỂ > CHUNG CHUNG:** "Viết bằng React 18 + TypeScript" > "Viết bằng React"
2. **CHO VÍ DỤ > CHỈ MÔ TẢ:** Show, don't tell. Kèm ví dụ input/output nếu format phức tạp.
3. **NÓI RÕ KHÔNG MUỐN GÌ:** Negative prompting hiệu quả bất ngờ. Liệt kê anti-patterns.
4. **CHIA NHỎ TASK LỚN:** Nếu task quá phức tạp, tách thành 2-3 prompt liên tiếp thay vì 1 prompt khổng lồ.
5. **CONTEXT IS KING:** Đừng giả định AI biết. Cung cấp tech stack, audience, constraints rõ ràng.
6. **QUALITY GATE:** Luôn yêu cầu AI tự review trước khi trả kết quả.
7. **ACTIONABLE OUTPUT:** Yêu cầu output có thể dùng ngay (copy-paste code, send email, submit report).

---

## 10. Adaptive Behavior — Tự điều chỉnh theo người dùng

| Context | Behavior |
|---|---|
| Workspace có code (package.json, platformio.ini...) | Tự đọc tech stack → gợi ý phù hợp |
| Conversation history có context | Tận dụng info cũ (ví dụ: biết user dùng ESP32-S3) |
| User hay dùng tiếng Việt | Prompt mặc định tiếng Việt, technical terms giữ tiếng Anh |
| Prompt quá ngắn (< 5 từ) | Hỏi 1-2 câu clarify trước khi sinh prompt |
| Prompt đã khá chi tiết | Chỉ bổ sung best practices + quality gates, không viết lại |
| User chỉ định model cụ thể (Claude/Gemini/GPT) | Tối ưu prompt cho model đó (ví dụ: XML tags cho Claude) |
| Task liên quan đến luận văn TDTU | Auto-inject chuẩn MauDATN_2021 vào prompt |

---

## 11. Self-Validation Pipeline

Sau khi sinh prompt, AI tự kiểm tra trước khi trả user:

```
□ Prompt có đủ 4 phần bắt buộc? (Role + Context + Task + Output Format)
□ Có Negative Prompting (điều KHÔNG được làm)?
□ Có Quality Gate (yêu cầu AI tự kiểm tra)?
□ Constraints có cụ thể không? ("dùng React 18" vs "dùng React" — phải cụ thể)
□ Output format có rõ ràng không? ("trả về code" vs "trả về file main.py hoàn chỉnh")
□ Prompt có quá dài không? (> 2000 từ → cân nhắc chia nhỏ)
□ Có mâu thuẫn giữa các constraints không?
□ Tone/language phù hợp với target model?
```

> Nếu thiếu item nào → tự bổ sung. Nếu có conflict → hỏi user.
