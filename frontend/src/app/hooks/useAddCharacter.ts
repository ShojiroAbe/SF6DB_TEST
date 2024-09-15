import useSWR from 'swr'

async function fetcher(key: string) {
  // keyにはエンドポイントが入ります
  return fetch(key).then((res) => res.json())
}

export const useAddCharacter = () => {
  const { data, error, isLoading } = useSWR(`${process.env.NEXT_PUBLIC_LOCAL_API_URL}/regist/character`, fetcher)

  console.log('data', data);
  console.log('error', error);
  console.log('isLoading', isLoading);


  return {
    data,
    error,
    isLoading
  }
}
