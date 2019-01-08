import r_b_hip_hop_songs


def test_query_maker():
    result = r_b_hip_hop_songs.query_maker("blah1", "blahblah2")
    assert result == "track: blah1 artist: blahblah2"

def test_no_features():
    result1 = r_b_hip_hop_songs.no_features("asf Featuring")
    result2 = r_b_hip_hop_songs.no_features("Post Malone Featuring 21 Savage")
    result3 = r_b_hip_hop_songs.no_features("DJ Khaled Featuring Justin Bieber, Quavo, Chance The Rapper & Lil Wayne")
    result4 = r_b_hip_hop_songs.no_features("Lady Gaga & Bradley Cooper")
    assert result1 == "asf"
    assert result2 == "post malone"
    assert result3 == "dj khaled"
    assert result4 == "lady gaga"
