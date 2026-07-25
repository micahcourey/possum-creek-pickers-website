export interface ShowItem {
  id: string;
  date: string;
  formattedDate: {
    month: string;
    day: string;
    year: string;
    dayOfWeek?: string;
  };
  time?: string;
  venue: string;
  city: string;
  state: string;
  ticketUrl?: string;
  status?: "Upcoming" | "Sold Out" | "Free Show" | "Festival";
  notes?: string;
}

export const shows: ShowItem[] = [
  {
    id: "2026-08-06-urban-stack",
    date: "Aug 6th, 2026",
    formattedDate: {
      month: "AUG",
      day: "06",
      year: "2026",
      dayOfWeek: "THU"
    },
    time: "7:00 PM",
    venue: "Urban Stack",
    city: "Chattanooga",
    state: "TN",
    status: "Upcoming",
    notes: "Live Acoustic Bluegrass Session"
  }
];
