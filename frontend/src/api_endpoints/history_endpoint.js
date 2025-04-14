async function fetchHistory(page, rowsPerPage) {
  try {
    const response = await fetch(
      `http://localhost:5000/history/?page=${page + 1}&limit=${rowsPerPage}`,
        {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            },
        }
    );

    console.log("Response:", response);

    if (!response.ok) {
      throw new Error('Failed to fetch history data');
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching history:', error);
    throw error;
  }
};

export default fetchHistory;