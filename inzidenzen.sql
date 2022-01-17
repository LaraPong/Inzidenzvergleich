-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 06. Jan 2022 um 11:46
-- Server-Version: 10.4.22-MariaDB
-- PHP-Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `inzidenzen`
--
CREATE DATABASE IF NOT EXISTS `inzidenzen` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `inzidenzen`;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_berlin`
--

CREATE TABLE `inzidenzen_deutschland_berlin` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_berlin`
--

INSERT INTO `inzidenzen_deutschland_berlin` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_berlin_mitte`
--

CREATE TABLE `inzidenzen_deutschland_berlin_mitte` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_berlin_mitte`
--

INSERT INTO `inzidenzen_deutschland_berlin_mitte` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_bremen`
--

CREATE TABLE `inzidenzen_deutschland_bremen` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_bremen`
--

INSERT INTO `inzidenzen_deutschland_bremen` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_dortmund`
--

CREATE TABLE `inzidenzen_deutschland_dortmund` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_dortmund`
--

INSERT INTO `inzidenzen_deutschland_dortmund` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_dresden`
--

CREATE TABLE `inzidenzen_deutschland_dresden` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_dresden`
--

INSERT INTO `inzidenzen_deutschland_dresden` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_duesseldorf`
--

CREATE TABLE `inzidenzen_deutschland_duesseldorf` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_duesseldorf`
--

INSERT INTO `inzidenzen_deutschland_duesseldorf` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_erfurt`
--

CREATE TABLE `inzidenzen_deutschland_erfurt` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_erfurt`
--

INSERT INTO `inzidenzen_deutschland_erfurt` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);
-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_essen`
--

CREATE TABLE `inzidenzen_deutschland_essen` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_essen`
--

INSERT INTO `inzidenzen_deutschland_essen` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);
-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_frankfurt`
--

CREATE TABLE `inzidenzen_deutschland_frankfurt` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_frankfurt`
--

INSERT INTO `inzidenzen_deutschland_frankfurt` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_hamburg`
--

CREATE TABLE `inzidenzen_deutschland_hamburg` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_hamburg`
--

INSERT INTO `inzidenzen_deutschland_hamburg` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_hannover`
--

CREATE TABLE `inzidenzen_deutschland_hannover` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_hannover`
--

INSERT INTO `inzidenzen_deutschland_hannover` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_kiel`
--

CREATE TABLE `inzidenzen_deutschland_kiel` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_kiel`
--

INSERT INTO `inzidenzen_deutschland_kiel` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_koeln`
--

CREATE TABLE `inzidenzen_deutschland_koeln` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_koeln`
--

INSERT INTO `inzidenzen_deutschland_koeln` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_magdeburg`
--

CREATE TABLE `inzidenzen_deutschland_magdeburg` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_magdeburg`
--

INSERT INTO `inzidenzen_deutschland_magdeburg` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_mainz`
--

CREATE TABLE `inzidenzen_deutschland_mainz` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_mainz`
--

INSERT INTO `inzidenzen_deutschland_mainz` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);
-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_muenchen`
--

CREATE TABLE `inzidenzen_deutschland_muenchen` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_muenchen`
--

INSERT INTO `inzidenzen_deutschland_muenchen` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_potsdam`
--

CREATE TABLE `inzidenzen_deutschland_potsdam` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_potsdam`
--

INSERT INTO `inzidenzen_deutschland_potsdam` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);
-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_saarbruecken`
--

CREATE TABLE `inzidenzen_deutschland_saarbruecken` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_saarbruecken`
--

INSERT INTO `inzidenzen_deutschland_saarbruecken` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);
-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_schwerin`
--

CREATE TABLE `inzidenzen_deutschland_schwerin` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_schwerin`
--

INSERT INTO `inzidenzen_deutschland_schwerin` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_stuttgart`
--

CREATE TABLE `inzidenzen_deutschland_stuttgart` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_stuttgart`
--

INSERT INTO `inzidenzen_deutschland_stuttgart` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `inzidenzen_deutschland_wiesbaden`
--

CREATE TABLE `inzidenzen_deutschland_wiesbaden` (
  `id` int(11) NOT NULL,
  `datum` date NOT NULL,
  `inzidenz` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Daten für Tabelle `inzidenzen_deutschland_wiesbaden`
--

INSERT INTO `inzidenzen_deutschland_wiesbaden` (`id`, `datum`, `inzidenz`) VALUES
(1, '2000-01-01', 111.1);

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `inzidenzen_deutschland_berlin`
--
ALTER TABLE `inzidenzen_deutschland_berlin`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_berlin_mitte`
--
ALTER TABLE `inzidenzen_deutschland_berlin_mitte`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_bremen`
--
ALTER TABLE `inzidenzen_deutschland_bremen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_dortmund`
--
ALTER TABLE `inzidenzen_deutschland_dortmund`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_dresden`
--
ALTER TABLE `inzidenzen_deutschland_dresden`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_duesseldorf`
--
ALTER TABLE `inzidenzen_deutschland_duesseldorf`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_erfurt`
--
ALTER TABLE `inzidenzen_deutschland_erfurt`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_essen`
--
ALTER TABLE `inzidenzen_deutschland_essen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_frankfurt`
--
ALTER TABLE `inzidenzen_deutschland_frankfurt`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_hamburg`
--
ALTER TABLE `inzidenzen_deutschland_hamburg`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_hannover`
--
ALTER TABLE `inzidenzen_deutschland_hannover`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_kiel`
--
ALTER TABLE `inzidenzen_deutschland_kiel`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_koeln`
--
ALTER TABLE `inzidenzen_deutschland_koeln`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_magdeburg`
--
ALTER TABLE `inzidenzen_deutschland_magdeburg`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_mainz`
--
ALTER TABLE `inzidenzen_deutschland_mainz`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_muenchen`
--
ALTER TABLE `inzidenzen_deutschland_muenchen`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_potsdam`
--
ALTER TABLE `inzidenzen_deutschland_potsdam`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_saarbruecken`
--
ALTER TABLE `inzidenzen_deutschland_saarbruecken`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_schwerin`
--
ALTER TABLE `inzidenzen_deutschland_schwerin`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_stuttgart`
--
ALTER TABLE `inzidenzen_deutschland_stuttgart`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `inzidenzen_deutschland_wiesbaden`
--
ALTER TABLE `inzidenzen_deutschland_wiesbaden`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_berlin`
--
ALTER TABLE `inzidenzen_deutschland_berlin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_berlin_mitte`
--
ALTER TABLE `inzidenzen_deutschland_berlin_mitte`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_bremen`
--
ALTER TABLE `inzidenzen_deutschland_bremen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_dortmund`
--
ALTER TABLE `inzidenzen_deutschland_dortmund`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_dresden`
--
ALTER TABLE `inzidenzen_deutschland_dresden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_duesseldorf`
--
ALTER TABLE `inzidenzen_deutschland_duesseldorf`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_erfurt`
--
ALTER TABLE `inzidenzen_deutschland_erfurt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_essen`
--
ALTER TABLE `inzidenzen_deutschland_essen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_frankfurt`
--
ALTER TABLE `inzidenzen_deutschland_frankfurt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_hamburg`
--
ALTER TABLE `inzidenzen_deutschland_hamburg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_hannover`
--
ALTER TABLE `inzidenzen_deutschland_hannover`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_kiel`
--
ALTER TABLE `inzidenzen_deutschland_kiel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_koeln`
--
ALTER TABLE `inzidenzen_deutschland_koeln`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_magdeburg`
--
ALTER TABLE `inzidenzen_deutschland_magdeburg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_mainz`
--
ALTER TABLE `inzidenzen_deutschland_mainz`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_muenchen`
--
ALTER TABLE `inzidenzen_deutschland_muenchen`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_potsdam`
--
ALTER TABLE `inzidenzen_deutschland_potsdam`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_saarbruecken`
--
ALTER TABLE `inzidenzen_deutschland_saarbruecken`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_schwerin`
--
ALTER TABLE `inzidenzen_deutschland_schwerin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_stuttgart`
--
ALTER TABLE `inzidenzen_deutschland_stuttgart`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT für Tabelle `inzidenzen_deutschland_wiesbaden`
--
ALTER TABLE `inzidenzen_deutschland_wiesbaden`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
