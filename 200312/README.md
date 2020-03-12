### 코딩테스트 연습 > 연습문제 > 문자열 내 마음대로 정렬하기   
[문제](https://programmers.co.kr/learn/courses/30/lessons/12915)  
- 각 문자열의 n번째 글자 기준 오름차순으로 단어 정렬(n번째 글자가 같을 땐 사전순 정렬)    

예시   

| strings | n | return |   
| --- | --- | --- |    
| [sun, bed, car] | 1 | [car, bed, sun] |  
| [abce, abcd, cdx] | 2 | [abcd, abce, cdx] |  

제한 사항  
- strings는 길이 1 이상, 50이하인 배열
- strings의 원소는 소문자 알파벳으로 이뤄짐  
- strings의 원소는 길이 1 이상, 100이하인 문자열입  
- 모든 strings의 원소의 길이는 n보다 큼  
- 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치  