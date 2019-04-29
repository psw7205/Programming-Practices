package homework2;

abstract class PairMap {
	protected String keyArray[]; // key를 저장하는 배열
	protected String valueArray[]; // value를 저장하는 배열

	abstract String get(String key); // key값을 가진 value 리턴, 없으면 null

	abstract void put(String key, String value); // key,value 쌍으로 저장, key가 중복되면 value수정

	abstract String delete(String key); // key를 가진 아이템 삭제, 삭제된 value 리턴

	abstract int length(); // 저장된 아이템의 개수 리턴
}

class Dictionary extends PairMap {
	int cnt;

	Dictionary(int in) {
		this.keyArray = new String[in];
		this.valueArray = new String[in];
		this.cnt = 0;
	}

	@Override
	String get(String key) {
		for (int i = 0; i < cnt; i++) {
			if (keyArray[i].equals(key)) {
				return valueArray[i];
			}
		}
		return null;
	}

	@Override
	void put(String key, String value) {

		for (int i = 0; i < cnt; i++) {
			if (keyArray[i].equals(key)) {
				valueArray[i] = value;
				return;
			}
		}

		keyArray[cnt] = key;
		valueArray[cnt] = value;
		cnt++;
		return;
	}

	@Override
	String delete(String key) {
		for (int i = 0; i < cnt; i++) {
			if (keyArray[i].equals(key)) {
				String str = valueArray[i];
				for (int j = i; j < keyArray.length - 1; j++) {
					keyArray[j] = keyArray[j + 1];
					valueArray[j] = valueArray[j + 1];
				}
				keyArray[cnt] = null;
				valueArray[cnt] = null;
				cnt--;
				return str;
			}
		}
		return null;
	}

	@Override
	int length() {
		return this.cnt;
	}

}

public class Hw2_1 {

	public static void main(String[] args) {
		Dictionary dic = new Dictionary(10);
		dic.put("황기태", "자바");
		dic.put("이재문", "파이썬");
		dic.put("이재문", "C++");
		System.out.println("이재문의 값은 " + dic.get("이재문"));
		System.out.println("황기태의 값은 " + dic.get("황기태"));
		dic.delete("황기태");
		System.out.println("황기태의 값은 " + dic.get("황기태"));

	}

}
