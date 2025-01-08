import gradio as gr


def merge_strings(japanese: str, korean: str) -> str:
    japanese_sentences: list[str] = list(filter(bool, japanese.replace("\u3000", "").split("\n")))
    korean_sentences: list[str] = list(filter(bool, korean.split("\n")))
    if len(japanese_sentences) != len(korean_sentences):
        return "error"

    markdown: list[str] = []
    for idx in range(len(japanese_sentences)):
        markdown_by_line: str = (
            f"""<p style="background-color: #ffffff; color: #1f1f1f; text-align: start;"
            data-ke-size="size18">
                <span style="font-family: 'Nanum Gothic';">
                    <b>{japanese_sentences[idx]}<br />
                    <span style="color: #131313; letter-spacing: 0px;">
                        <span style="color: #ef5369;">{korean_sentences[idx]}</span><br />
                    </span>
                    </b>
                </span>
            </p><br>"""
        )
        markdown.append(markdown_by_line)
    return "\n".join(markdown)


with gr.Blocks() as demo:
    gr.Markdown("# 블로그 JPOP 번역 패스트트랙")

    with gr.Row():
        a_input: gr.Textbox = gr.Textbox(label="일본어", placeholder="일본어 가사 입력")
        b_input: gr.Textbox = gr.Textbox(label="한국어", placeholder="한국어 번역 가사 입력")

    result: gr.Textbox = gr.Textbox(label="결과물", interactive=False)

    merge_button: gr.Button = gr.Button("결과물 출력")

    # with gr.Row():
    #     copy_a_button = gr.Button("A 복사")
    #     copy_b_button = gr.Button("B 복사")
    #     copy_result_button = gr.Button("결과 복사")

    # 이벤트
    merge_button.click(merge_strings, inputs=[a_input, b_input], outputs=result)

    # # 복사 버튼 클릭 이벤트 (복사된 텍스트는 브라우저의 클립보드로 이동)
    # copy_a_button.click(None, [], None, js="() => copyToClipboard(document.querySelector('[label=\\'a_input\\'] input').value)")
    # copy_b_button.click(None, [], None, js="() => copyToClipboard(document.querySelector('[label=\\'문자열 B\\'] input').value)")
    # copy_result_button.click(None, [], None, js="() => copyToClipboard(document.querySelector('[label=\\'결과물\\'] input').value)")

demo.launch()
