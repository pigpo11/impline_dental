const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

const regex = /<footer id="map">[\s\S]*?<\/footer>/;
const replacement = `<footer class="main-new-footer">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 40px;">
            <!-- 상단: 지도와 정보 표 -->
            <div class="info-grid">
                <div class="info-map image-placeholder">
                    <!-- 우측 상단 지도(약도) 이미지 위치 -->
                </div>
                <div class="info-styled-table">
                    <div class="info-row first-row">
                        <div class="info-label">주소</div>
                        <div class="info-value">
                            서울특별시 송파구 백제고분로 198, GM빌딩 2층(9호선 삼전역 3번 출구 앞)<br>
                            <a href="#" class="info-btn">네이버지도바로가기 —</a>
                        </div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">주차</div>
                        <div class="info-value">
                            발렛파킹 - 건물 주차장 입구에서 비상등을 켜주세요<br>
                            (발렛파킹 불가 시 전화로 문의해주세요 02 415 2080)
                        </div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">진료시간</div>
                        <div class="info-value times-grid">
                            <div class="time-col">화·수·금</div><div class="time-col">9:30 ~ 18:30</div>
                            <div class="time-col">월·목</div><div class="time-col">9:30 ~ 20:30</div>
                            <div class="time-col">토요일</div><div class="time-col">9:30 ~ 14:00</div>
                            <div class="time-col">점심시간</div><div class="time-col">13:00 ~ 14:00</div>
                        </div>
                    </div>
                    <div class="info-row last-row" style="border-bottom: 2px solid #333;">
                        <div class="info-label">예약상담</div>
                        <div class="info-value">
                            <div class="tel-number" style="font-size: 20px; font-weight: 500; margin-bottom: 12px; color: #222;">02 415 2080</div>
                            <div class="btn-group">
                                <a href="#" class="info-btn">네이버예약 —</a>
                                <a href="#" class="info-btn">카카오톡 상담 —</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 가로 라인 구분(전체 너비 적용) -->
            <div class="footer-divider"></div>

            <!-- 하단: 카피라이트 텍스트 영역 -->
            <div class="footer-bottom-info">
                <p>한걸음더치과의원 | 대표원장: 김규태 | 사업자등록번호 518-25-01274 | T. 02 415 2080 | F. 02 415 2081</p>
                <p>서울특별시 송파구 백제고분로 198, GM빌딩 2층</p>
                <p class="copyright" style="margin-top: 5px;">© 2022 한걸음더치과의원. All Rights Reserved</p>
            </div>
        </div>
    </footer>`;

content = content.replace(regex, replacement);
fs.writeFileSync('index.html', content, 'utf8');
console.log('Replaced footer in index.html');
