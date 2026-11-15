# TDM Travel Assistant

## Student Information

- Full name:
- Student ID:
- Guide coverage: Thủ Dầu Một, using the city's boundaries before 2025.

## Test Results

Questions and recorded application responses are kept in Vietnamese. Correctness labels for tests 1–6 reflect the recorded manual evaluation; retrieval evidence still needs to be recorded.

| No. | Question | Expected ID / Answer | Actual Answer | Actual Retrieved IDs | Correct / Incorrect | Failure Stage and Evidence |
|---|---|---|---|---|---|---|
| 1 | Chùa Hội Khánh được xây dựng năm nào? | G01; 1741 | 1741 [G01] | Not recorded yet | Correct | No answer error reported; retrieval evidence pending. |
| 2 | Chùa Ông Ngựa còn có những tên gọi nào? | G04; Thanh An Tự, Quan Đế Miếu | Thanh An Tự hoặc Quan Đế Miếu [G04] | Not recorded yet | Correct | No answer error reported; retrieval evidence pending. |
| 3 | Bảo tàng Bình Dương nằm ở địa chỉ nào? | G09; 565 Đại lộ Bình Dương | 565 Đại lộ Bình Dương, khu vực Thủ Dầu Một [G09] | Not recorded yet | Correct | No answer error reported; retrieval evidence pending. |
| 4 | Người ta bắt đầu xây chùa Hội Khánh vào năm bao nhiêu? | G01; 1741 | 1741 [G01] | Not recorded yet | Correct | No answer error reported; retrieval evidence pending. |
| 5 | Giá vé vào chùa Hội Khánh hôm nay là bao nhiêu? | No supporting entry; admit the information is unavailable | Tôi không biết vì bộ hướng dẫn chưa có thông tin này. | Not recorded yet | Correct | Correct refusal; retrieval evidence pending. |
| 6 | Cảng nhà rồng ở đâu? | No supporting entry; admit the information is unavailable | Tôi không biết vì bộ hướng dẫn chưa có thông tin này. | Not recorded yet | Correct | Correct refusal; retrieval evidence pending. |
| 7 | Chùa Hội Khánh xây dựng năm nào, chùa Ông Ngựa còn tên gì, Bảo tàng Bình Dương ở đâu và đình Tân An được công nhận di tích quốc gia ngày nào? | G01: 1741; G04: Thanh An Tự, Quan Đế Miếu; G09: 565 Đại lộ Bình Dương; G13: April 26, 2014 | Not run yet | Not recorded yet | Not evaluated | Tests coverage of four required entries with k=3; classify any failure only after observing the result. |

### Recording Retrieval Evidence

- For each question, open the retrieved-source panel and record all three IDs in the displayed order, including for questions that receive an "I don't know" response.
- Copy the actual answer and retrieved IDs from the same run. Answer citations alone do not identify every retrieved entry.
- Test 7 is an additional multi-part test. Its expected failure has not been established by a run.
- For the demonstration video, select one observed success and one observed failure. Explain whether the failure occurred in missing data, retrieval, or generation. A correct refusal for an out-of-guide question is a success.

## Installation and Usage

Requires Python and a running Ollama server exposed through Pinggy.
The server must have `embeddinggemma` and `qwen3:4b` installed.

```bash
python -m pip install -r requirements.txt
```

Create `.env` from `.env.example`, then set:

- `FIREBASE_API_KEY`: the Firebase project's Web API key.
- `OLLAMA_BASE_URL`: the current HTTPS Pinggy URL.

Enable Email/Password in Firebase Authentication.

```bash
python -m streamlit run app.py
```

## Known Limitations

- Answers are limited to the 20 guide entries.
- Top-3 retrieval may miss evidence for multi-part questions.
- Chat history is displayed but is not included in subsequent model prompts.
- Source-only answering is prompt-based and can still fail.
- Colab sessions and Pinggy tunnels may disconnect.
- Firebase token expiration is not automatically handled.

## AI Assistance

ChatGPT assisted with implementation guidance, debugging,
drafting the knowledge base, and preparing documentation
and the video outline.

## Demonstration Video

[Watch the demonstration](https://drive.google.com/file/d/18Ya2efguEIPEuygkyulf51SESQW8GIOi/view?usp=sharing)