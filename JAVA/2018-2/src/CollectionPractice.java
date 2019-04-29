import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.Vector;
// array 대체 순차적으로 저장 
// 랜덤억세스 가능
// 중간에 삽입 시 한칸씩 다 뒤로 미루고 삽입, 삭제 시 전부 한칸 씩 앞으로 당김

public class CollectionPractice {

	public static void func(String[] a) {
		for (String ar : a)
			System.out.println(ar);
	}

	public static void main(String[] args) {

		Vector<Integer> v = new Vector<>();

		v.add(10); // boxing 중... int를 Integer로 바꿈......
		v.add(20);
		v.add(40);
		v.set(2, 30); // 2번째 인덱스 값을 30으로
		v.add(1, 15); // 1번째 인덱스 앞에 15추가
		v.remove(0); // 0번째 인덱스 값 삭제

		for (int i = 0; i < v.size(); i++)
			System.out.println(v.get(i));

		for (Integer e : v)
			System.out.println(e);

		ArrayList<String> v2 = new ArrayList<>();

		v2.add("박상우");
		v2.add("세종");
		v2.add("대학교");
		v2.add("소프트웨어학과");
		v2.remove("소프트웨어학과"); // 원하는 데이터도 삭제 가능

		for (String str : v2)
			System.out.println(str);

		System.out.println(v2.indexOf("대학교")); // 같은 문자열을 찾아 인덱스 리턴

		String[] arr = new String[v2.size()];

		v2.toArray(arr); // String 배열로 변환
		func(arr);

		LinkedList<String> v3 = new LinkedList<>();

		v3.add("박상우");
		v3.add("세종");
		v3.add("대학교");
		v3.add("소프트웨어학과");
		
		for (String str : v3) // 읽기전용 foreach문은 상관 없지만
			System.out.println(str);

		for (int i = 0; i < v3.size(); i++)
			System.out.println(v3.get(i)); //링크드리스트에서 일반적인 for문처럼 작성하면 안됨, 맨 마지막 인자까지 접근하는데 O(n^2)
		// 순차접근의 문제점
		
		Iterator<String> it = v3.iterator(); // iterator를 사용
		
		while(it.hasNext() == true) // 다음 데이터가 있는 동안
		{
			String e = it.next(); // 다음 데이터로 이동하고 e에 저장 
			System.out.println("iterator : " + e); // 출력
		}
		
		
		LinkedList<Integer> v4 = new LinkedList<>();
		
		v4.add(0);
		v4.add(1);
		v4.add(2);
		v4.add(3);
		
		for(int e : v4)
			System.out.println(e);
		
		Iterator<Integer> it2 = v4.iterator(); // 처음은 빈공간을 가르킴
		
		System.out.println("==" + it2.next()); // 다음으로 it2 이동
		it2.remove();
		
		for(int e : v4)
			System.out.println(e);
		
////////////////////////////////////////////////////////////////
		//Collections의 static 함수로 알고리즘 사용 가능

		Collections.sort(v3); // 정렬
		for (String str : v3)
			System.out.println(str);
		
		Collections.reverse(v3); // 역순으로 정렬
		for (String str : v3)
			System.out.println(str);
	}
}
