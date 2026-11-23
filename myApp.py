import streamlit as st
st.set_page_config(page_title="문서 작성 예제", layout="centered")

# 제목

st.title("📘 Streamlit 문서 작성 예제")

# 섹션

st.header("1. 기본 텍스트 출력")

st.write("이것은 `st.write()`를 사용한 텍스트입니다.")
st.text("이것은 형식 없는 텍스트입니다.")

# 마크다운 사용

st.markdown("**굵은 글씨**와 *기울임 글씨* 사용하기")
st.markdown("> 인용구 스타일")

# 코드 블록 출력

st.code("""
def hello():
print("Hello, Streamlit!")
""", language='python')


# 표 출력

# st.header("2. 표 출력")
# import pandas as pd
# df = pd.DataFrame({
# "이름": ["홍길동", "이몽룡"],
# "나이": [29, 34]
# })
# st.dataframe(df)

# 이미지 출력

# st.header("3. 이미지 출력")

# st.image("data:image/webp;base64,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", width=300)


name = st.text_input("이름을 입력하세요")
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120)
birthdate = st.date_input("생년월일 선택")
hobby = st.selectbox("취미 선택", ["독서", "운동", "게임", "음악"])
agree = st.checkbox("이용 약관에 동의합니다")
file = st.file_uploader("파일 업로드")

if st.button("제출"):
    st.success(f"{name}님({age}세), 제출 완료!")

    st.title("📋 사용자 정보 입력 폼")

# 1. 사용자 입력 위젯

name = st.text_input("🧑 이름을 입력하세요")
age = st.number_input("🎂 나이를 입력하세요", min_value=0, max_value=120, step=1)
gender = st.radio("🚻 성별을 선택하세요", ["남자", "여자", "기타"])
interests = st.multiselect("💡 관심 있는 주제를 선택하세요", ["인공지능", "데이터 분석", "웹 개발", "금융", "디자인"])
description = st.text_area("📘 자기소개 또는 하고 싶은 말")
agree = st.checkbox("✅ 개인정보 수집 및 이용에 동의합니다")

# 2. 제출 버튼

if st.button("제출2"):
    if not name:
        st.warning("이름을 입력하세요.")
elif not agree:
    st.error("개인정보 수집 동의가 필요합니다.")
else:
# 3. 결과 출력
    st.success("입력이 완료되었습니다! 🎉")
    st.markdown("---")
    st.subheader("📄 제출 내용 요약")
    st.write(f"**이름:** {name}")
    st.write(f"**나이:** {age}세")
    st.write(f"**성별:** {gender}")
    st.write(f"**관심 주제:** {', '.join(interests) if interests else '없음'}")
    st.write("**소개글:**")
    st.info(description if description else "작성하지 않음")

st.title("📘 Streamlit 문서 작성 예제")