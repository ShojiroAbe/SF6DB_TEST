import useSWR from 'swr'

// 環境変数行き予定
const API_URL = 'http://localhost:8000'

async function fetcher(key: string) {
  // keyにはエンドポイントが入ります
  return fetch(key).then((res) => res.json())
}

export const useGetCharacter = () => {
  const { data, error, isLoading } = useSWR(`${API_URL}/get/character`, fetcher)

  console.log('data', data);
  console.log('error', error);
  console.log('isLoading', isLoading);

  return {
    data,
    error,
    isLoading
  }
}
